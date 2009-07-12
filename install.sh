#!/bin/bash
plasmapkg -r awsplasmoid
rm -i awsplasmoid.zip
zip -r awsplasmoid.zip . -x .git\*
plasmapkg -i awsplasmoid.zip
plasmoidviewer awsplasmoid
