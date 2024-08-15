# fdds/utils/monitoring.py

import time

class QueryAnalytics:
    def __init__(self):
        self.query_logs = []

    def log_query(self, query, start_time, end_time):
        """
        Logs the execution time of a query.
        
        :param query: The FDQL query executed.
        :param start_time: The start time of the query execution.
        :param end_time: The end time of the query execution.
        """
        execution_time = end_time - start_time
        self.query_logs.append({
            'query': query,
            'execution_time': execution_time
        })

    def get_performance_report(self):
        """
        Generates a report of query performance.
        
        :return: A performance report.
        """
        total_time = sum(log['execution_time'] for log in self.query_logs)
        average_time = total_time / len(self.query_logs) if self.query_logs else 0
        return {
            'total_queries': len(self.query_logs),
            'total_time': total_time,
            'average_time': average_time
        }

class Monitoring:
    def __init__(self):
        self.query_analytics = QueryAnalytics()

    def monitor_query(self, query_function, *args, **kwargs):
        """
        Monitors the performance of a query execution.
        
        :param query_function: The function that executes the query.
        :param args: Arguments for the query function.
        :param kwargs: Keyword arguments for the query function.
        :return: The result of the query execution.
        """
        start_time = time.time()
        result = query_function(*args, **kwargs)
        end_time = time.time()

        self.query_analytics.log_query(query_function.__name__, start_time, end_time)
        return result
