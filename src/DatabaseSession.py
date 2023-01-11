from cassandra.cluster import Cluster, ExecutionProfile, ConsistencyLevel, EXEC_PROFILE_DEFAULT
from cassandra.policies import LoadBalancingPolicy
from cassandra.query import named_tuple_factory
from uuid import UUID
from collections import namedtuple

from DatabaseObject import DatabaseObject


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
            retry_policy=LoadBalancingPolicy(),
            consistency_level=ConsistencyLevel.LOCAL_QUORUM,
            serial_consistency_level=ConsistencyLevel.LOCAL_SERIAL,
            request_timeout=15,
            row_factory=named_tuple_factory,
        )

        cluster = Cluster(
            contact_points=CLUSTER_NODES,
            port=9042,
            execution_profiles={EXEC_PROFILE_DEFAULT: exec_profile},
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

    def add(self, obj: DatabaseObject):
        self.session.execute(obj.add_to_database())

    def remove(self, obj: DatabaseObject):
        self.session.execute(obj.delete_from_database())

    def update(self, obj: DatabaseObject):
        self.session.execute(obj.update_data())

    def get(self, _id: UUID, table_name: str, table_id_col: str = None) -> namedtuple:
        return self.session.execute(
            f"""
            SELECT * FROM {table_name}
            WHERE {table_id_col if table_id_col != None else f'{table_name[0]}_id'} = {str(_id)};
            """
        ).one()

    def find_all(self, table_name: str) -> list[namedtuple]:
        return list(self.session.execute(f"SELECT * FROM {table_name};"))

    def find_by(self, table_name: str, where_sql_clause: str) -> list[namedtuple]:
        return list(self.session.execute(f"SELECT * FROM {table_name} WHERE {where_sql_clause} ALLOW FILTERING;"))
