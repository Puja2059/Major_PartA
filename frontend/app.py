
from pathlib import Path
import runpy
import sys


def main():


    if "streamlit" in sys.modules:
        from streamlit.runtime.scriptrunner import get_script_run_ctx
        if get_script_run_ctx(suppress_warning=True) is not None:
            import streamlit as st
            st.title("Start the shared NitiShield workspace")
            st.info("Stop this Streamlit server with Ctrl+C. In VS Code, choose Run and Debug > NitiShield, or run the command below. Both open http://localhost:8501/#dashboard with your saved workspace.")
            launcher = Path(__file__).resolve().parents[1] / "start.ps1"
            st.code(f'& "{launcher}"', language="powershell")
            return
    backend = Path(__file__).resolve().parents[1] / "Backend"
    sys.path.insert(0, str(backend))
    runpy.run_path(str(backend / "app.py"), run_name="__main__")


if __name__ == "__main__":
    main()
