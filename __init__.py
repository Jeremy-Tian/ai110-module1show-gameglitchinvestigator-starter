# AI collaboration: When pytest failed with ModuleNotFoundError, we identified that
# the project wasn't set up as a proper Python package. Together we added __init__.py
# files to make the directories proper packages that pytest can import from.
# Game Glitch Investigator Package