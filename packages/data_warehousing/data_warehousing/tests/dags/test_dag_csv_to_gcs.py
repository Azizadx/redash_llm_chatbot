import unittest
from datetime import datetime
from airflow.models import DagBag


class TestCsvToGcsDag(unittest.TestCase):
    def setUp(self):
        self.dagbag = DagBag(
            dag_folder='dags', include_examples=False)

    def test_dag_loading(self):
        dag_id = 'csv_2_gcs'
        dag = self.dagbag.get_dag(dag_id)
        self.assertIsNotNone(dag)
        self.assertEqual(len(dag.tasks), 1)

    def test_task_dependencies(self):
        dag_id = 'csv_2_gcs'
        dag = self.dagbag.get_dag(dag_id)
        dependencies = {
            'upload_csv_to_gcs': [],
        }

        for task_id, upstream_task_ids in dependencies.items():
            task = dag.get_task(task_id)
            upstream_tasks = set(dag.get_task(upstream_task_id)
                                 for upstream_task_id in upstream_task_ids)
            self.assertEqual(set(task.upstream_task_ids), upstream_tasks)


if __name__ == '__main__':
    unittest.main()
