# Fast Dynamic Database System (FDDS)

FDDS is an advanced, fully custom-built database system designed to offer a rich set of features while being user-friendly and performant. It eliminates the need for traditional SQL databases by providing its own query language (FDQL), optimized storage, and extensive functionality tailored for developers who need both power and simplicity.

## Features

- **Custom Query Language (FDQL):** SQL-like syntax with full command support for data definition, manipulation, and querying.
- **Advanced Data Structures:** Supports complex data types, graph data modeling, and BLOB storage.
- **Transactions and Concurrency:** ACID compliance with transaction management and optimistic concurrency control.
- **Indexing and Query Optimization:** Supports B-trees, hash indexes, and full-text search indexes.
- **Backup and Recovery:** Automatic backups with point-in-time recovery.
- **Security:** User authentication, role-based access control, and data encryption.
- **Cross-Platform Compatibility:** Fully implemented in Python, compatible with Windows, macOS, and Linux.

Set up the environment:

Install the required Python packages:
"python setup_environment.py"

Run the Application:

Start the Flask server:
"python -m fdds.api.api_layer"

Usage
Upload a File
To upload a file:
bash
Copy code
{curl -X POST http://127.0.0.1:5000/api/upload_file -F "image=@path/to/your/file.ext"}

Download a File
To download a file:
bash
Copy code
{curl -O http://127.0.0.1:5000/api/download_file/your_file.ext}

Delete a File
To delete a file:
bash
Copy code
{curl -X DELETE http://127.0.0.1:5000/api/delete_file/your_file.ext}

Execute FDQL Query
To execute an FDQL query:
bash
Copy code
{curl -X POST http://127.0.0.1:5000/api/query -H "Content-Type: application/json" -d "{\"query\": \"YOUR FDQL QUERY HERE\"}"}

Contributing
We welcome contributions! Please open an issue or submit a pull request.

Contact
If you have any questions or need further assistance, please contact Arif Hussain at starrvarse@gmail.com

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/starrvarse/fdds-software.git
   cd fdds-software
## Python integration
      https://pypi.org/project/fdds/
      pip install fdds
