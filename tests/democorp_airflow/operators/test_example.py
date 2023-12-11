from democorp_airflow.operators.example import ExampleOperator


def test_exampleoperator():
    test = ExampleOperator(task_id="test")
    test.execute(context={})
