import os
import platform
import pyperclip
import streamlit as st
from damj import Damj
from streamlit_file_browser import st_file_browser
from streamlit_tags import st_tags

from utils import new_line

# Page Config
st.set_page_config(
    page_title="Damj Platform",
    page_icon="🧊",
)


# Session State
if 'prompt' not in st.session_state:
    st.session_state.prompt = ""
if 'damj' not in st.session_state:
    st.session_state.damj = None
if 'path' not in st.session_state:
    st.session_state.path = None
if "ui_prompt" not in st.session_state:
    st.session_state.ui_prompt = ""

# Logo
LOGO = os.path.join("assets", "logo_small.png")
LOGO_HORIZ = os.path.join("assets", "logo_small.png")
st.logo(LOGO_HORIZ, icon_image=LOGO)
st.html("""
<style> img[data-testid="stLogo"]
{ height: 3rem; width: auto; margin-left: 0.5rem; margin-right: 0.5rem; }
</style>
""")

# Title & Description
st.html("<h1 align='center'>Damj Platform</h1>")
st.write("""
Welcome to the Damj Platform! This platform is designed to help you manage your files and data 
and generate prompts with ease. You can use the file browser to navigate through your files and
the tags to categorize your prompts.
""")
st.divider()

st.html("<h3 align='center'>Project Path</h2>")
st.info("""
If you are running the platform using **Docker**, make sure to write the correct path by writing **`/mnt/`** before the path. 
E.g. if you did deploy by `docker run --name damj_platform -p 7878:7878 -v /Users/username/Projects/:/mnt/Projects damj`, you should write `/mnt/Projects` as the path.
""")
path = st.text_input("Project Path", label_visibility='collapsed', placeholder="E.g. C:/Users/Username/Documents/Project")
st.divider()

if path:

    if not os.path.exists(path):
        st.error("Invalid path. Please provide a valid path.")
        st.stop()

    st.session_state.path = path
    project_files = os.listdir(path)

    st.header("File Browser")
    event = st_file_browser(
            path, use_static_file_server=True, show_choose_file=True, show_download_file=True,
            show_new_folder=True, show_upload_file=True, use_cache=True
            )
    st.divider()

    # Initialize Damj
    whitelist_files = st_tags(
        label="###### Whitelist Files",
        text="Press Enter to add a tag",
        value=[],
        suggestions=project_files,
    )

    blacklist_files = st_tags(
        label="###### Blacklist Files",
        text="Press Enter to add a tag",
        value=[],
        suggestions=project_files,
    )

    st.markdown("##### Snippet Marker")
    snippet_marker = st.selectbox(
        "Snippet Marker", label_visibility='collapsed', 
        options=["```", "'''", '"""'], index=0
        )
    
    st.session_state.damj = Damj(
        cwd=path,
        whitelist_files=whitelist_files,
        blacklist_files=blacklist_files,
        snippet_marker=snippet_marker
    )
    st.divider()

    # Project Information
    st.header("Project Information")
    new_line(2)
    project_overview = st.text_area("Project Overview", value="", height=100)
    new_line(2)
    col1, col2, col3 = st.columns([1,0.1,1], gap='large')
    with col1:
        st.subheader("Project Structure")
        new_line()
        add_project_structure = col1.checkbox("Add Project Structure", value=True)
        new_line()
        add_files_content = col1.checkbox("Add Files Content", value=False)
        if add_files_content:
            with col2:
                st.html(
                '''
                    <div class="divider-vertical-line2"></div>
                    <style>
                        .divider-vertical-line2 {
                            border-left: 2px solid rgba(49, 51, 63, 0.2);
                            height: 250px;
                        }
                    </style>
                '''
            )

            with col3:
                st.subheader("Files Content Options")
                new_line()
                add_comments = col3.checkbox("Add Comments", value=False)
                add_imports = col3.checkbox("Add Imports", value=False)
                add_docstrings = col3.checkbox("Add Docstrings", value=False)
                ipynb_output = col3.checkbox("IPython Notebook Output", value=False)

    try:
        st.session_state.damj.project_info(
            project_overview=project_overview,
            add_project_structure=add_project_structure,
            add_files_content=add_files_content,
            py_options={
                "add_comments": add_comments,
                "add_imports": add_imports,
                "add_docstrings": add_docstrings,
                "ipynb_output": ipynb_output
            }
        )
    except Exception as e:
        st.session_state.damj.project_info(
            project_overview=project_overview,
            add_project_structure=add_project_structure,
            add_files_content=add_files_content,
            py_options={
                "add_comments": False,
                "add_imports": False,
                "add_docstrings": False,
                "ipynb_output": False
            }
        )

    st.divider()
    st.header("Create Prompt")
    question = st.text_area("Ask Question", value="", height=100, key="question")
    if question:
        prompt = st.session_state.damj.create_prompt(question=question)
        st.session_state.damj.prompt = prompt



    # SIDEBAR PROMPT GENERATOR
    if st.session_state.damj is not None:
        with st.sidebar:
            if not platform.system() == "Linux":
                col1, col2, col3 = st.columns([1, 3, 1])
                if col2.button("Copy to Clipboard", use_container_width=True):
                    pyperclip.copy(st.session_state.ui_prompt)
                    st.toast("Copied to clipboard!", icon="🌟", )
            st.header("Prompt Generator")
            prompt, markdown = st.tabs(["  󠁪 󠁪 󠁪 󠁪 󠁪 󠁪 󠁪 󠁪 󠁪 Prompt 󠁪 󠁪 󠁪 󠁪 󠁪  󠁪 󠁪 󠁪 󠁪 󠁪  ", "  󠁪 󠁪 󠁪 󠁪 󠁪 󠁪 󠁪 󠁪 󠁪Markdown 󠁪 󠁪 󠁪 󠁪 󠁪 󠁪 󠁪 󠁪 󠁪 󠁪  "])
            with prompt:
                ui_prompt = st.text_area("Prompt", st.session_state.damj.prompt, height=950, label_visibility='hidden')
                if ui_prompt:
                    st.session_state.ui_prompt = ui_prompt
            with markdown:
                with st.container(height=950, border=False):
                    st.markdown(st.session_state.ui_prompt)
