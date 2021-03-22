check-manifest --update
pause
del dist\* /Q /S /F
pause
python setup.py bdist_wheel sdist
pause
python -m twine check dist/*
pause
echo "Next step - uploading to pypi!"
pause
python -m twine upload dist/*
pause