import binaryninja as bn
import glob


def execute_plugin(bv, name):
    plugin_context = bn.plugin.PluginCommandContext(bv)
    plugins = bn.plugin.PluginCommand.get_valid_list(plugin_context)

    target_plugin = plugins[name];

    if target_plugin != None:
        target_plugin.execute(plugin_context)

    return None

def open_glob_binaryview(directory):
    
    return None
