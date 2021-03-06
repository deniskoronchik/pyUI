﻿
"""
-----------------------------------------------------------------------------
This source file is part of OSTIS (Open Semantic Technology for Intelligent Systems)
For the latest info, see http://www.ostis.net

Copyright (c) 2010 OSTIS

OSTIS is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OSTIS is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with OSTIS.  If not, see <http://www.gnu.org/licenses/>.
-----------------------------------------------------------------------------
"""


'''
Created on 09.02.2010

@author: Pavel Karpan
'''

import suit.core.kernel as core
import os
import text_viewer
import text_editor

def initialize():
    
    kernel = core.Kernel.getSingleton()
    
    from suit.core.objects import Factory
    import suit.core.keynodes as keynodes
    
    global view_factory
    global edit_factory
    
    view_factory = Factory(viewer_creator)
    edit_factory = Factory(editor_creator)
    kernel.registerViewerFactory(view_factory, [keynodes.ui.format_term,
                                                keynodes.ui.format_string,
                                                keynodes.ui.format_int,
                                                keynodes.ui.format_real])
    
    kernel.registerEditorFactory(edit_factory, [keynodes.ui.format_term,
                                                keynodes.ui.format_string,
                                                keynodes.ui.format_int,
                                                keynodes.ui.format_real])

def shutdown():
    global view_factory
    global edit_factory
    kernel = core.Kernel.getSingleton()
    kernel.unregisterViewerFactory(view_factory)
    kernel.unregisterEditorFactory(edit_factory)
    
def viewer_creator():
    return text_viewer.TextViewer() 

def editor_creator():
    return text_editor.TextEditor()