from pydantic import BaseModel

class KubernetesCase(BaseModel):
    pod_status: str
    cpu_usage: int
    memory_usage: int
    restart_count: int
    deployment_change: bool
    node_pressure: bool
    error_log: str

    root_cause: str | None = None
    solution: str | None = None

    status: str = "unresolved"
