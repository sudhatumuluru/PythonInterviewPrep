#!/usr/bin/env python
# -*- coding: utf-8 -*-
podBayDoorStatus = 'open'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
podBayDoorStatus = "I\'m sorry, Dave. I\'m afraid I can't do that.'"
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open" please open  .'

# An assertion is a sanity check to make sure your code isn’t doing something obviously wrong.
# If the sanity check fails, then an AssertionError exception is raised.
# Second display statemnt is executed