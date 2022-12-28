from cassandra.cluster import Cluster, ExecutionProfile, ConsistencyLevel, EXEC_PROFILE_DEFAULT
from cassandra.policies import DowngradingConsistencyRetryPolicy
from cassandra.query import tuple_factory

class DatabaseSession():
    """Fabryka sesji korzystania z bazy danych"""

    def __init__(self):
        CLUSTER_NODES = [
            '172.17.0.2',
            '172.17.0.3',
        ]

        STRATEGY = 'SimpleStrategy'
        REP_FACTOR = 2

        exec_profile = ExecutionProfile(
            retry_policy=DowngradingConsistencyRetryPolicy(),
            consistency_level=ConsistencyLevel.LOCAL_QUORUM,
            serial_consistency_level=ConsistencyLevel.LOCAL_SERIAL,
            request_timeout=15,
            row_factory=tuple_factory,
        )

        cluster = Cluster(
            contact_points=CLUSTER_NODES,
            port=9042,
            execution_profiles={ EXEC_PROFILE_DEFAULT: exec_profile },
        )

        self.session = cluster.connect()

        self.session.execute(
            """
            CREATE KEYSPACE IF NOT EXISTS nierelacyjne
            WITH replication = { 'class': %s, 'replication_factor': %s }
            """,
            (STRATEGY, REP_FACTOR)
        )

        self.session.set_keyspace('nierelacyjne')
