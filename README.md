# 🎣 devpath: The Zero-Config Python Development Hook

**devpath** is a minimal, ultra-efficient utility designed to eliminate development friction when testing Python packages. It provides an instant, self-configuring "editable install" experience without requiring external command-line tools like `pip install -e .` or complex environments.

## ✨ Philosophy: Install-and-Go Debugging

The primary goal of **devpath** is to ensure that code changes made in your source files are **immediately available** upon `import`. This is achieved by leveraging a core Python mechanism to prioritize your development directory over the installed package.

**Forget the console commands—just import and develop.**

## ⚙️ How It Works: The `sys.path` Injection (Direct Import)

The core of `devpath` is a single, concise function executed upon module import.

1.  **Automatic Detection:** When you run `import devpath`, the logic automatically searches upwards from the execution directory for the local development folder (named **`paks_repo`**).
2.  **Path Hook:** It injects the path to your source folder into the beginning of the Python's global **`sys.path`** list.
3.  **Priority:** Because the source folder is now a top-level location, all subsequent imports (e.g., `import pak1`) will find and load the **source code version** (the one you are currently editing) instead of the installed package version.

### Benefits

* **Zero Configuration:** No `pip install -e .` necessary in your workflow.
* **Instant Updates:** Code changes are reflected immediately on re-execution.
* **Minimal Footprint:** The entire library is one file (`__init__.py`).

## 🚀 Usage

### 1. Installation

Install the hook once in your development environment:

```bash
pip install devpath

### 2. Structure

Your project needs this structure to work:

```text
📦 Proyect_folder/ (The project root)
├── 📝 my_test_script.py  <-- Your test script that runs the code.
|
└── 📁 paks_repo/         <-- Your SOURCE CODE that you edit.
    ├── 📦 pak1/           <-- Your package (e.g., your library code).
    │   ├── __init__.py
    │   └── code.py
    │
    └── 📦 pak2/
        └── ... (Other packages in development)

# In my_test_script.py
import devpath             # 1. Activates the hook.
import pak1                # 2. Imports your package directly.

pak1.run_my_new_feature() 
# ... Modify pak1/code.py and run the script again—the new code is instantly loaded.
