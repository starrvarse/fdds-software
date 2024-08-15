# fdds/cli/fdds_cli.py

import argparse
from fdds.core.engine import FDDSEngine
from fdds.fdql.parser import FDQLParser
from fdds.fdql.commands import FDQLExecutor

class FDDSCli:
    """
    Command-Line Interface for FDDS.
    Allows users to interact with the FDDS system from the terminal.
    """

    def __init__(self):
        self.engine = FDDSEngine()
        self.parser = FDQLParser()
        self.executor = FDQLExecutor(self.engine)

    def run(self):
        """
        Runs the CLI, parsing and executing user commands.
        """
        parser = argparse.ArgumentParser(description="FDDS Command-Line Interface")
        parser.add_argument('command', help="FDQL command to execute", nargs=argparse.REMAINDER)
        
        args = parser.parse_args()
        fdql_command = " ".join(args.command)
        
        try:
            parsed_command = self.parser.parse(fdql_command)
            result = self.executor.execute(parsed_command)
            print(result)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    cli = FDDSCli()
    cli.run()
