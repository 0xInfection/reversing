## Instructions

The following contains simple instructions on how to build the site **manually**. Automated deployments are done by GitHub Actions every week.

### Install the deps
On your system, you'll require the following dependencies:
- You'll need Git.
- You'll need Python > 3.6 atleast.
    - Run `python3 -m pip install bs4 html2markdown selenium requests`
    - Python dependencies are resolved and are required for the `scraper.py`.
- You'll need Node.js < 12 (Node.js v10.x should be fine).
    - Simple `apt install nodejs && apt install npm` does the job.
    - Next you'll require `gitbook 3.x.x` - `npm install -g gitbook`.
- All dependencies are resolved.

### Build and deploy ¯\_(ツ)_/¯
- Run `gitbook_publish.sh`. Everything will happen automagically. Usually takes 3-4 mins to complete the task, build and finally deploy.