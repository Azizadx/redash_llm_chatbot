import unittest
from datetime import datetime
from airflow.models import DagBag


class TestConnectionGcpDag(unittest.TestCase):

    def setUp(self):
        self.dagbag = DagBag(
            dag_folder='dags', include_examples=False)

    def test_dag_loading(self):
        dag_id = 'connection_gcp'
        dag = self.dagbag.get_dag(dag_id)
        self.assertIsNotNone(dag)
        self.assertEqual(len(dag.tasks), 1)

    def test_task_exists(self):
        dag_id = 'connection_gcp'
        task_id = 'check_connection'
        dag = self.dagbag.get_dag(dag_id)
        task = dag.get_task(task_id)
        self.assertIsNotNone(task)


if __name__ == '__main__':
    unittest.main()
