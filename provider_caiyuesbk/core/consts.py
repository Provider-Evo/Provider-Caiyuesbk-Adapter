


from __future__ import annotations

import asyncio

BASE_URL = "https://caiyuesbk.top:16188"
CHAT_PATH = "/v1/chat/completions"

# 硬编码兜底模型列表
MODELS: list[str] = [
    "Qwen3-32B-siliconflow",
    "glm-4.6-siliconflow",
    "qwen3-80b",
    "kimi-k2",
    "kimi-k2-thinking",
    "deepseek-v3.1-terminus",
    "deepseek-v3.1",
    "deepseek-v3.2-siliconflow",
    "glm4.7",
    "kimi-k2-instruct-0905",
    "qwen3.5-122b",
    "gpt-oss-120b",
    "glm-4.6V-siliconflow",
    "kimi-k2-siliconflow",
]

# 能力配置
CAPS: dict[str, bool] = {
    "chat": True,
    "completions": True,
    "responses": True,
    "tools": True,
    "native_tools": True,
    "thinking": True,
    "vision": True,
}

# 是否允许远程模型列表覆盖本地（True=覆盖，False=只增不减）
FETCH_MODELS_ENABLED: bool = True

# 远程模型刷新间隔（秒），默认 24 小时
MODEL_FETCH_INTERVAL: int = 86400

async def sleep_before_retry(attempt: int, max_retries: int, logger) -> None:
    """指数退避等待。"""
    wait = 1.0 * (2 ** (attempt - 1))
    logger.warning("caiyuesbk 第 %d/%d 次重试，等待 %.1fs", attempt, max_retries, wait)
    await asyncio.sleep(wait)

