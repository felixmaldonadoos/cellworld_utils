#!/bin/bash

function gh_copilot_suggest(){
    # Check if an argument is provided
    if [ -z "$1" ]
    then
        echo "No argument provided. Please provide an argument."
        return 1
    fi

    # set variable "command" to "gh copilot suggest" followed by the argument passed to the function
    command="gh copilot suggest $1"
    echo $command
    # run the command 
    $command
}

# Call the function with the first command-line argument
gh_copilot_suggest $1