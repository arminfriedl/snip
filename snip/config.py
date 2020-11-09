"""
Snip Configuration
==================

Configure snip based on settings found in the environment or environment
specific config files. The variables are set in the following order (later
settings override earlier ones):
- .snipenv
- .snipenv.[SNIP_STAGE]
- environment
- config.py (defaults)

SNIP_STAGE is the only special value. It is taken from definitions in the
following order (later settings override earlier ones):
- .snipenv
- environment
- parameter in `config.configure`

If no SNIP_STAGE is found in any of them, no stage specific configuration
(.snipenv.[SNIP_STAGE]) file is taken into account.

All known configuration variables can be found in `SnipConfig`.
"""

import os
import logging
from typing import Literal, Optional
from pathlib import Path

from pydantic import BaseModel
from pydantic.types import SecretStr

log = logging.getLogger(__name__)

class SnipConfig(BaseModel):
    # Database settings
    SNIP_DATABASE: Literal['sqlite', 'postgres', 'mysql']
    SNIP_DATABASE_URI: str
    SNIP_DATABASE_TRACK_MODIFICATION: bool = False

    # Flask settings
    SNIP_FLASK_ENVIRONMENT: Literal['development', 'production'] = 'production'
    SNIP_FLASK_DEBUG: bool = False
    SNIP_FLASK_SKIP_DOTENV: int = 1
    SNIP_FLASK_PREFERRED_URL_SCHEME: Literal['http', 'https'] = 'https'
    # Non-standard flask settings
    SNIP_FLASK_HOST: str = "localhost"
    SNIP_FLASK_PORT: int = 5000
    SNIP_FLASK_PROXYFIX: bool = False

    # Snip settings
    SNIP_STAGE: Optional[str]
    SNIP_SECRET: SecretStr # also used as flask's SECRET_KEY
    SNIP_KEYLEN: int = 5

def configure(stage: Optional[str] = None) -> SnipConfig:
    config_dict = {}

    # Read common configuration from .snipenv
    config_dict.update(read_base_env())

    # bootstrap configuration, try to determine stage first
    # stage can be set from parameter or environment
    if not stage:
        if os.getenv("SNIP_STAGE"):
            stage = os.getenv("SNIP_STAGE")
        elif config_dict.get("SNIP_STAGE"):
            stage = config_dict.get("SNIP_STAGE")

    # Read stage configuration from .snipenv.[stage] if set
    if stage: config_dict.update(read_stage_env(stage))
    else: log.debug("Not using stage configuration")

    # Read variables from environment
    config_dict.update(os.environ)

    return SnipConfig(**config_dict)

def read_base_env() -> dict:
    """ Read base configuration from .snipenv if it exists """
    base_env_path = Path(".snipenv")
    log.debug(f"Reading .snipenv file from {base_env_path.resolve()}")

    try:
        base_env_dict = read_env(base_env_path)
        log.info("Setting base config from .snipenv")
        return base_env_dict
    except FileNotFoundError:
        log.debug(".snipenv file not found")
        return {}

def read_stage_env(stage: str) -> dict:
    """ Reads the .snipenv file of the current stage """
    log.info(f"Using stage configuration for {stage}")
    stage_env_name = ".snipenv."+stage
    stage_env_path = Path(stage_env_name)
    log.debug(f"Reading .snipenv file from {stage_env_path.resolve()}")

    try:
        stage_env_dict = read_env(stage_env_path)
        log.info(f"Setting stage config from {stage_env_name}")
        return stage_env_dict
    except FileNotFoundError:
        log.error(f"Could not find stage configuration for {stage_env_name} in {os.path.curdir}")
        raise

def read_env(env_path: Path) -> dict:
    """ Read env file from path into dict """
    if not env_path.exists() or not env_path.is_file():
        raise FileNotFoundError

    env_dict = dict()
    with open(env_path) as f:
        for (idx, line) in enumerate(f):
            # skip empty lines
            if not line.strip(): continue
            # skip comment lines
            if line.startswith('#'): continue

            try:
                (k, v) = map(str.strip, line.split('=', maxsplit=1))
                env_dict[k] = v
            except:
                log.error(f"Cannot parse {env_path}:{idx}:{line}")
                raise
    return env_dict
