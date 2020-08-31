# EasyPluginBot
This repo is a fairly modular, yet easy to use implementation of
[discord.py][dpy].
Its main purpose is to work as an extension handler.
### Table of Contents
1. [Basic Setup](#basic-setup)
2. [Editing config.json](#editing-configjson)
3. [Adding Keys and Tokens](#adding-keys-and-tokens)
4. [Using Extensions](#using-extensions)
5. [Writing New Extensions](#writing-new-extensions)
6. [Reporting Bugs](#reporting-bugs)
7. [Help With Development](#help-with-development)

#### Basic Setup
To use this framework, you need at least Python 3.6, though the
[latest version][pydown] is recommended. <br>
If you are on Linux, you probably don't need to install [Python][py].

Once you have [Python][py] installed, you need to install
[discord.py][dpy]. To do so, navigate to wherever you cloned this repo
and run the following command:
```
pip install -r requirements.txt
```
Now that everything is installed, try running the bot. You can either use
your file manager and double-click on `run.py`, or you can run it from
the terminal.

#### Editing config.json
Most of what makes this framework so modular is the extension management,
but part of that comes from the `config.json` file.

To configure the basic settings of this bot, navigate to the `core/`
folder and open `config.json`. You should see something like this:
```json
{
  "bot":{
    "no_ext_abort" : true,
    "command_prefix" : "!",
    "ext_dir" : "extensions",
    "owner_ids" : [600130839870963725,499211108138090507],
    "links" : {
      "GitHub" : "https://github.com/FourInchKnife/EasyPluginBot/"
    },
    "max_error_length" : 1000
  }
}
```

Here's a breakdown of what everything controls:

| Parameter Name | Description | Type  |
| :---:          | :---        | :---: |
| no_ext_abort   | Toggles whether the bot runs even without any extensions loaded | `bool` |
| command_prefix | The prefix used to call commands from Discord | `string` |
| ext_dir | Selects the directory to search for extensions | `string` |
| owner_ids | Sets the Discord ID for the owner of the bot | `List[integer]` |
| links | Links to websites relevant to the bot | `Dictionary[string:string]` |
| max_error_length | The maximum length of an error before it is sent in a file as an attachment | `integer` |

In the `config.json` you might also have to configure settings for
specific cogs. To do this, use this format:

```json
{
  "bot":{
    "Settings here":"..."
  },
  "ext":{
    "FileName":{
      "CogName":{
        "Settings here":"..."
      }
    }
  }
}
```

Each bot plugin should come with its own readme to tell you what config
settings it needs.

#### Adding Keys and Tokens

Adding your Discord bot token to this program is very similar to editing
the `config.json` file. All you have to do is create the `core/keys.json`
file and put this text into it:
```json
{
  "bot":"token here",
  "ext":{
    "FileName":{
      "CogName":"key/token"
    }
  }
}
```
If you do this, the program won't ask you to input your token at every
startup, and will instead use whatever you put into the file. All
extensions should tell you what tokens they use.

#### Using Extensions

Using extensions is super easy. Paste it into the extension folder
(`extensions/` by default). That's it. When you run the bot, it will
search through the folder and try to load all `.py` files. If any file
fails to load, the program will ignore it and move on.

#### Writing New Extensions

To write new extensions, write all code in a command in a
[cog][dpycogs]. I'm not going to write a Python tutorial or a
[discord.py][dpy] tutorial, so you will need to look into that yourself
if you're clueless.

After you finish writing your extension, add the `Cogs` variable. It
must be a list containing all of the cogs in the file.

#### Reporting Bugs

Just [open a new issue][issue] on the EasyPluginBot GitHub page. Make
sure you include the version of Python, discord.py, and EasyPluginBot.
If you get a traceback, include that as well. If it's an issue with one
of the example plugins, don't start an issue. The example plugins are
not updated.

#### Help With Development

As of right now, there is no mechanism for helping out other than just
using pull requests in GitHub.

[issue]: https://github.com/FourInchKnife/EasyPluginBot/issues/new/choose "Make a new iissue for the EasyPluginBot GitHub"
[dpy]: https://github.com/Rapptz/discord.py/ "GitHub for discord.py"
[dpydocs]: https://discordpy.readthedocs.io/ "Documentation for Discord.py"
[py]: https://python.org/ "The Official Python Website"
[pydown]: https://python.org/downloads/
[dpycogs]: https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html?highlight=cogs "discord.py Cogs"
