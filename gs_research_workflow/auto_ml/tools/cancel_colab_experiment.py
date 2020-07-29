# -*- coding: utf-8 -*-
"""
取消一个已经在运行的 colab tasks
"""
import asyncio
import logging
logger = logging.getLogger(__name__)


async def cancel_colab_tasks_by_group_name(experiment_name: str):
    from gs_framework.service import StatelessService
    from gs_framework.colab.colab_pool_client import ColabPoolClient
    from gs_framework.colab.colab_pool_0_constants import Configuration as colab_config
    from gs_framework.activatable_stateful_service import Env
    import faust.types

    class _ColabPoolService(StatelessService):
        def __init__(self, pool_client: ColabPoolClient, _):
            super().__init__()
            self._pool_client: ColabPoolClient = pool_client
            self.add_service_units(pool_client)

        async def start(self):
            await super().start()
            await self._pool_client.get_ready()

    class _ColabPoolCallEnv(Env):
        def __init__(self, trial_uuid: str):
            super().__init__()
            self.trial_uuid = trial_uuid

        async def cancel_tasks_by_group_name(self, task_group_name: str):
            pool_client = ColabPoolClient(colab_config.pool_name, colab_config.pool_env_rpc_callee_topic)
            pool_client.pool_env_status_stream.bind(topic_define=colab_config.pool_env_status_topic)
            pool_client.rpc_caller_stream.bind(topic_define=colab_config.pool_client_rpc_caller_topic)

            pool_test_service = _ColabPoolService(pool_client, self.trial_uuid)
            await pool_test_service.start()
            logger.info(f"_ColabPoolService service started")

            await asyncio.sleep(10)
            cancelled = await pool_client.cancel_task_group(task_group_name)
            logger.info(f"{task_group_name} cancelled: {cancelled}")

    colab_caller_env = _ColabPoolCallEnv("abcde")
    colab_caller_env.bind(topic_define=faust.types.TP(topic="nni_colab_pool_0", partition=1))
    await colab_caller_env.start()
    await colab_caller_env.cancel_tasks_by_group_name(experiment_name)
    await asyncio.sleep(60)  # 因为是 submit ，这里为了安全，只 sleep 1min


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(cancel_colab_tasks_by_group_name("EquityDailyReturnCSBert_ChnV1"))

