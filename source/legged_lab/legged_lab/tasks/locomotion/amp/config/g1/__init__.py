import gymnasium as gym

from . import agents

from legged_lab.tasks.locomotion.amp.amp_env import AmpEnv

gym.register(
    id="LeggedLab-Isaac-AMP-Rough-G1-v0",
    entry_point="legged_lab.tasks.locomotion.amp.amp_env:AmpEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.amp_rough_env_cfg:G1AmpRoughEnvCfg",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:G1RoughRslRlOnPolicyRunnerAmpCfg",
    },
)

gym.register(
    id="LeggedLab-Isaac-AMP-Rough-G1-Play-v0",
    entry_point="legged_lab.tasks.locomotion.amp.amp_env:AmpEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.amp_rough_env_cfg:G1AmpRoughEnvCfg_PLAY",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:G1RoughRslRlOnPolicyRunnerAmpCfg",
    },
)

gym.register(
    id="LeggedLab-Isaac-AMP-Flat-G1-v0",
    entry_point="legged_lab.tasks.locomotion.amp.amp_env:AmpEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.amp_flat_env_cfg:G1AmpFlatEnvCfg",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:G1FlatRslRlOnPolicyRunnerAmpCfg",
    },
)

gym.register(
    id="LeggedLab-Isaac-AMP-Flat-G1-Play-v0",
    entry_point="legged_lab.tasks.locomotion.amp.amp_env:AmpEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.amp_flat_env_cfg:G1AmpFlatEnvCfg_PLAY",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.rsl_rl_ppo_cfg:G1FlatRslRlOnPolicyRunnerAmpCfg",
    },
)