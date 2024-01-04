import unittest
from datetime import datetime
from airflow.models import DagBag


class TestCreateTableDag(unittest.TestCase):

    def setUp(self):
        self.dagbag = DagBag(
            dag_folder='dags', include_examples=False)

    def test_dag_loading(self):
        dag_id = 'create_table'
        dag = self.dagbag.get_dag(dag_id)
        self.assertIsNotNone(dag)
        self.assertEqual(len(dag.tasks), 3)

    def test_task_dependencies(self):
        dag_id = 'create_table'
        dag = self.dagbag.get_dag(dag_id)
        dependencies = {
            'create_traffic_dataset': [],
            'gcs_to_raw': ['create_traffic_dataset'],
            'check_load': ['gcs_to_raw'],
        }

        for task_id, upstream_task_ids in dependencies.items():
            task = dag.get_task(task_id)
            upstream_tasks = set(dag.get_task(upstream_task_id)
                                 for upstream_task_id in upstream_task_ids)
            self.assertEqual(set(task.upstream_task_ids), upstream_tasks)

    def test_task_instances(self):
        dag_id = 'create_table'
        dag = self.dagbag.get_dag(dag_id)
        task_instances = {
            'create_traffic_dataset': 1,
            'gcs_to_raw': 1,
            'check_load': 1,
        }

        for task_id, expected_instances in task_instances.items():
            task = dag.get_task(task_id)
            self.assertEqual(len(task.get_instances()), expected_instances)


if __name__ == '__main__':
    unittest.main()
