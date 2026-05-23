from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Text,
    Index
)

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class KubernetesCase(Base):
    __tablename__ = "cases"
    __table_args__ = (

        Index(
            "idx_candidate_retrieval",
            "pod_status",
            "deployment_change",
            "node_pressure"
        ),

    )

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    pod_status = Column(String(100))
    cpu_usage = Column(Integer)
    memory_usage = Column(Integer)
    restart_count = Column(Integer)
    deployment_change = Column(Boolean)
    node_pressure = Column(Boolean)
    error_log = Column(Text)

    root_cause = Column(Text)
    solution = Column(Text)