INSERT INTO cases (
    pod_status,
    cpu_usage,
    memory_usage,
    restart_count,
    deployment_change,
    node_pressure,
    error_log,
    root_cause,
    solution
)
VALUES

(
    'CrashLoopBackOff',
    92,
    95,
    14,
    TRUE,
    FALSE,
    'OOMKilled container',
    'memory leak',
    'increase memory limit'
),

(
    'Running',
    98,
    70,
    0,
    FALSE,
    FALSE,
    'high CPU throttling detected',
    'cpu bottleneck',
    'scale deployment replicas'
),

(
    'ImagePullBackOff',
    10,
    20,
    5,
    TRUE,
    FALSE,
    'image not found',
    'wrong image tag',
    'fix image tag'
),

(
    'Pending',
    15,
    30,
    0,
    FALSE,
    TRUE,
    'insufficient memory',
    'node resource exhausted',
    'add worker node'
),

(
    'CrashLoopBackOff',
    85,
    90,
    11,
    TRUE,
    FALSE,
    'segmentation fault detected',
    'application crash',
    'rollback deployment'
),

(
    'Running',
    70,
    40,
    0,
    FALSE,
    FALSE,
    'connection timeout redis',
    'redis unavailable',
    'restart redis service'
),

(
    'Running',
    88,
    50,
    1,
    FALSE,
    FALSE,
    'database connection timeout',
    'database overload',
    'scale database instance'
),

(
    'Error',
    40,
    35,
    7,
    TRUE,
    FALSE,
    'configmap missing',
    'missing configuration',
    'recreate configmap'
),

(
    'Pending',
    20,
    25,
    0,
    FALSE,
    TRUE,
    'node disk pressure',
    'disk full',
    'cleanup node disk'
),

(
    'CrashLoopBackOff',
    93,
    96,
    20,
    TRUE,
    FALSE,
    'java heap space',
    'heap overflow',
    'increase JVM heap size'
);