# -*- coding: utf-8 -*-

"""模拟启动测试 Desktop Env 需要用到的 service 环境"""
import asyncio
import logging
import os

from gs_desktop_envs.envs.chrome_stateful_envs import ChromeDesktopEnv
from gs_framework.debug_utilities import start_stateless_srv, INST, start_stateful_srv
from gs_framework.platform_srv.dce_prop_dtypes import StatefulSrv, StatefulSrvSubscription

from gs_research_workflow.webpage_related_workflow.web_ui_objects_related_srvs import UrlGroupDCESrv, \
    WebUIObjectsManageEnv

logger = logging.getLogger(__name__)


async def start_all_srvs(email: str):
    logger.info("start UrlGroupDCESrv service")
    _url_group_stateless_srv = await start_stateless_srv(INST(UrlGroupDCESrv))

    logger.info("start WebUIObjectsManageEnv service")

    _ui_objects_manage_env = await start_stateful_srv(StatefulSrv(INST(WebUIObjectsManageEnv, acct_id=email),
                                                                  srv_subscription=[
                                                                      StatefulSrvSubscription("chrome_desktop_env",
                                                                                              INST(ChromeDesktopEnv,
                                                                                                   email,
                                                                                                   os.uname().nodename))]
                                                                  ))


async def main():
    await start_all_srvs("laigen.soso@gmail.com")
    await asyncio.sleep(3600.0)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

