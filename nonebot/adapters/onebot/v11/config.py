"""OneBot v11 适配器配置项。

FrontMatter:
    sidebar_position: 2
    description: onebot.v11.config 模块
"""

from typing import Optional

from pydantic import Field, AnyUrl, BaseModel
from nonebot.compat import PYDANTIC_V2, ConfigDict

from nonebot.adapters.onebot.utils import WSUrl


class Config(BaseModel):
    """OneBot 配置类。"""

    onebot_access_token: Optional[str] = Field(
        default=None, alias="onebot_v11_access_token"
    )
    """OneBot 协议授权令牌"""
    onebot_secret: Optional[str] = Field(default=None, alias="onebot_v11_secret")
    """OneBot HTTP 上报数据签名口令"""
    onebot_ws_urls: set[WSUrl] = Field(default_factory=set, alias="onebot_v11_ws_urls")
    """OneBot 正向 Websocket 连接目标 URL 集合"""
    onebot_api_roots: dict[str, AnyUrl] = Field(
        default_factory=dict, alias="onebot_v11_api_roots"
    )
    """OneBot HTTP API 请求地址字典"""

    if PYDANTIC_V2:
        model_config = ConfigDict(populate_by_name=True)
    else:

        class Config:
            allow_population_by_field_name = True
