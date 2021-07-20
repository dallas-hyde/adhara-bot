from discord.ext import commands
import cogs.base
import cogs.planetside


# By subclassing commands.Bot it allows us to define our own behavior for events that we would otherwise have to use decorators for
class AdharaBot(commands.Bot):
    async def on_ready(self):
        print(f"Logged in as: {self.user}")


# This function is used to get the bot's login token stored in a file at the supplied path
def get_login_token(path):
    login_token = None

    try:
        file = open(path)
        login_token = file.read()
        file.close()
    
    except FileNotFoundError:
        print("Login token could not be retrieved!")
        print("'{0}' does not exist!".format(path))
    
    except Exception as exc:
        print("Unhandled exception!")
        print(exc)

    return login_token


LOGIN_TOKEN = get_login_token("token.txt")

# If the login token is not None and is not empty, create the bot
if LOGIN_TOKEN != None and LOGIN_TOKEN != "":
    bot = AdharaBot(command_prefix="*", case_insensitive=True)

    # TODO: Load bot cogs
    bot.add_cog(cogs.base.Base(bot))
    bot.add_cog(cogs.planetside.Planetside(bot))
        
    bot.run(LOGIN_TOKEN)
        
else:
    print("Bot could not be created!")
