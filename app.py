from telethon import TelegramClient, events, sync
from telethon.tl.types import InputChannel, InputPeerUser
import yaml
import sys
from telethon.sessions import StringSession
import logging
import  configparser
import  json, requests
from threading import Thread
from  telethon  import  TelegramClient , events
from  telethon . errors  import  SessionPasswordNeededError
import os
import  telethon . sync
import subprocess
import asyncio,time
from  pprint  import  pprint
from bs4 import BeautifulSoup
import urllib.request,urllib
        

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("telethon").setLevel(level=logging.WARNING)
logger = logging.getLogger(__name__)

def start(config):
    client = TelegramClient(
        StringSession(config["session_name"]
                      ), config["api_id"], config["api_hash"]
    )
    client.start()

    @client.on(events.NewMessage(pattern="/pylang"))
    async def add_py(event):
#         if str(event.sender_id) in os.environ.get("sender_id"):

        msg = event.message.message
        if os.environ.get("sender_id")==str(event.sender_id):
            await event.edit(msg+"\n\n"+"__"+"Running python command . . .__")
        else:
            await event.reply("__Running python command . . .__")
        try:
            code = msg.lstrip('/pylang')
        except IndexError:
            if os.environ.get("sender_id")==str(event.sender_id):
                await event.edit(msg+"\n\n"+"__"+"No arguments given (py) ...__")
            else:
                await event.reply("__No arguments given (py) ...__")

        command = "".join(f"\n {x}" for x in code.split("\n.strip()"))
        indexofip = command.find("py_input_vars")
        ip = ""
        if indexofip != -1:
            user_in = command[indexofip+len("py_input_vars:"):].strip()
            command = command[:indexofip]
            ip = user_in.encode("utf-8")
        # skipcq: BAN-B603
        """
            print(input())
            py_input_vars:
            1 2 3 4 5
            3 4 5 6 7
            
        """

        data = {
            "lang": "python3",
            "code": command,
            "input": ip
        }

        result = json.loads(requests.post(
            "https://compilethis.herokuapp.com/", data=data).content).get("result")

        if len(result) > 2500:
            if os.environ.get("sender_id")==str(event.sender_id):
                await event.edit(msg+"\n\n"+"__"+"Result is too big .. send as file__")
            else:
                await event.reply("__Result is too big .. send as file__")
                
            with open("output.txt", "w+") as f:
                f.write(result)
            await client.send_file(event.chat_id, 'output.txt')
            os.remove("output.txt")
        else:
            # time.sleep(2)
            try:
                if os.environ.get("sender_id")==str(event.sender_id):
                    await event.edit(msg+"\n\n"+"="*[20,max(len(result),12)][len(result)<20]+"\n"+"__OUTPUT:__\n\n**"+result+" **")
                else:
                    await event.reply("** "+result+" **")
            except Exception as excp:
                if os.environ.get("sender_id")==str(event.sender_id):
                    await event.edit(msg+"\n\n"+"="*[20,max(len(str(excp)),12)][len(str(excp))<20]+"\n"+"__ERROR:__\n\n**"+str(excp)+" **")
                else:
                    await event.reply("** "+str(excp)+" **")

    @client.on(events.NewMessage(pattern="/cpplang"))
    async def add_cpp(event):
#         if str(event.sender_id) in os.environ.get("sender_id"):

        msg = event.message.message
        await event.edit(msg+"\n\n"+"__"+"Running cpp command . . ."+"__")
        try:
            code = msg.lstrip('/cpplang')
        except IndexError:
            await event.edit(msg+"\n\n"+"__"+"No arguments given (cpp) ...__")
        command = "".join(f"\n {x}" for x in code.split("\n.strip()"))
        indexofip = command.find("cpp_input_vars")
        ip = ""
        if indexofip != -1:
            user_in = command[indexofip+len("cpp_input_vars:"):].strip()
            command = command[:indexofip]
            ip = user_in.encode("utf-8")
        # skipcq: BAN-B603
        """
            cout << "hello" << endl;
            cpp_input_vars:
            1 2 3 4 5
            3 4 5 6 7
        """

        data = {
            "lang": "cpp",
            "code": command,
            "input": ip
        }

        result = json.loads(requests.post(
            "https://compilethis.herokuapp.com/", data=data).content).get("result")

        if len(result) > 2500:
            await event.edit(msg+"\n\n"+"__"+"Result is too big .. send as file__")
            with open("output.txt", "w+") as f:
                f.write(result)
            await client.send_file(event.chat_id, 'output.txt')
            os.remove("output.txt")
        else:
            try:
                if os.environ.get("sender_id")==str(event.sender_id):
                    await event.edit(msg+"\n\n"+"="*[20,max(len(result),12)][len(result)<20]+"\n"+"__OUTPUT:__\n\n**"+result+" **")
                else:
                    await event.reply("** "+result+" **")
            except Exception as excp:
                if os.environ.get("sender_id")==str(event.sender_id):
                    await event.edit(msg+"\n\n"+"="*[20,max(len(str(excp)),12)][len(str(excp))<20]+"\n"+"__ERROR:__\n\n**"+str(excp)+" **")
                else:
                    await event.reply("** "+str(excp)+" **")

    @client.on(events.NewMessage(pattern="/clang"))
    async def add_c(event):
#         if str(event.sender_id) in os.environ.get("sender_id"):

        msg = event.message.message
        await event.edit(msg+"\n\n"+"__"+"Running c command . . ."+"__")
        try:
            code = msg.lstrip('/clang')
        except IndexError:
            await event.edit(msg+"\n\n"+"__"+"No arguments given (c) ...__")
        command = "".join(f"\n {x}" for x in code.split("\n.strip()"))
        indexofip = command.find("c_input_vars")
        ip = ""
        if indexofip != -1:
            user_in = command[indexofip+len("c_input_vars:"):].strip()
            command = command[:indexofip]
            ip = user_in.encode("utf-8")
        # skipcq: BAN-B603
        """
            printf("hello");
            c_input_vars:
            1 2 3 4 5
            3 4 5 6 7

        """

        data = {
            "lang": "c",
            "code": command,
            "input": ip
        }

        result = json.loads(requests.post(
            "https://compilethis.herokuapp.com/", data=data).content).get("result")

        if len(result) > 2500:
            await event.edit(msg+"\n\n"+"__"+"Result is too big .. send as file__")
            with open("output.txt", "w+") as f:
                f.write(result)
            await client.send_file(event.chat_id, 'output.txt')
            os.remove("output.txt")
        else:
            try:
                if os.environ.get("sender_id")==str(event.sender_id):
                    await event.edit(msg+"\n\n"+"="*[20,max(len(result),12)][len(result)<20]+"\n"+"__OUTPUT:__\n\n**"+result+" **")
                else:
                    await event.reply("** "+result+" **")
            except Exception as excp:
                if os.environ.get("sender_id")==str(event.sender_id):
                    await event.edit(msg+"\n\n"+"="*[20,max(len(str(excp)),12)][len(str(excp))<20]+"\n"+"__ERROR:__\n\n**"+str(excp)+" **")
                else:
                    await event.reply("** "+str(excp)+" **")

    @client.on(events.NewMessage(pattern="/animate"))
    async def text_list_animate(event):
                
        msg = event.message.message
        await event.edit(msg+"\n\n"+"__"+"Running animate command . . ."+"__")
        try:
            code = msg.lstrip('/animate')
        except IndexError:
            await event.edit(msg+"\n\n"+"__"+"No arguments given (c) ...__")
        command = "".join(f"\n {x}" for x in code.split("\n.strip()"))
        time_out = 60
        result = []
        if '-t' in command:
            result = (command.split('-t')[0]).split(',')
            try:
                time_out = int(command.split('-t')[1].strip())
            except:
                time_out = 60
        else:
            result = command.split(',')
        result = list(map(lambda x:x.strip(),result))
#         print(result)
        if len(result) > 2500:
            await event.edit(msg+"\n\n"+"__"+"Result is too big .. send as file__")
            with open("output.txt", "w+") as f:
                f.write(result)
            await client.send_file(event.chat_id, 'output.txt')
            os.remove("output.txt")
        else:
            try:
                indexofresult,st = 0,time.time()
                while(time.time()-st<time_out):
                    await event.edit(str(result[indexofresult]))
                    time.sleep(0.6)
                    indexofresult+=1
                    if indexofresult>=len(result):
                        indexofresult = 0
            except Exception as excp:
                await event.edit(msg+"\n\n"+"="*[20,max(len(str(excp)),12)][len(str(excp))<20]+"\n"+"__ERROR:__\n\n**"+str(excp)+" **")
                
    @client.on(events.NewMessage(pattern="/gitinfo"))
    async def git_user_info(event):
        msg = event.message.message
        LENGTH = 30
        try:
            
            await event.edit(msg+"\n\n"+"__"+"Running Git Info Command . . ."+"__")
            try:
                code = msg.lstrip('/gitinfo')
            except IndexError:
                await event.edit(msg+"\n\n"+"__"+"No arguments given (gitinfo) ...__")
            command = "".join(f"\n {x}" for x in code.split("\n.strip()"))
            username = command.strip()
            
            url = "https://github.com/"

            page = urllib.request.urlopen(url+username)

            soup = BeautifulSoup(page,"html.parser")

            result = []
            result.append("Username: "+username)

            no_of_repo,no_of_followers,no_of_following,bio,status,profile_img,contributions_last_year,no_of_stars = None,None,None,None,None,None,None,None
            
            try:
                no_of_repo = soup.find('span',{'class':'Counter'}).text
                result.append("Number of repos:"+" "*(LENGTH-len(no_of_repo)-len("Number of repos:"))+no_of_repo)
            except:
                pass
            try:
                no_of_followers = soup.find('a',{'href':'/'+username+'?tab=followers'}).find('span').text
                result.append("Number of followers:"+" "*(LENGTH-len(no_of_followers)-len("Number of followers:"))+no_of_followers)
            except:
                pass
            try:
                no_of_following = soup.find('a',{'href':'/'+username+'?tab=following'}).find('span').text
                result.append("Number of following:"+" "*(LENGTH-len(no_of_following)-len("Number of following:"))+no_of_following)
            except:
                pass
            try:
                no_of_stars = soup.find('a',{'href':'/'+username+'?tab=stars'}).find('span').text
                result.append("Number of stars:"+" "*(LENGTH-len(no_of_stars)-len("Number of stars:"))+no_of_stars)
            except:
                pass
            try:
                bio = soup.find('div',{'class':'user-profile-bio'}).find('div').text.strip().split()
                bio_list = []
                for bio_word in bio:
                    if bio_word.strip():
                        bio_list.append(bio_word)
                result.append(username+"'s bio: "+" ".join(bio_list))
            except:
                pass
            try:
                status = soup.find('div',{'class':'user-status-message-wrapper'}).find('div',{'class':''}).text.strip().split()
                status_list = []
                for status_word in status:
                    if status_word.strip():
                        status_list.append(status_word)
                result.append(username+"'s status: "+" ".join(status_list))
            except:
                pass
            try:
                profile_img = soup.find('img',{'alt':'@'+username})['src']
                result.append("Profile pic URL: "+profile_img)
            except:
                pass
            try:
                contributions_last_year = soup.find('div',{'class':'js-yearly-contributions'}).find('h2').text.strip().split()
                contributions_last_year_list = []
                for contributions in contributions_last_year:
                    if contributions.strip():
                        contributions_last_year_list.append(contributions)
                result.append("Contributions: "+" ".join(contributions_last_year_list))
            except:
                pass
            # print(no_of_repo,no_of_followers,no_of_following,bio,status,contributions_last_year,profile_img)
            result = "\n".join(result)


#             print(result)
            if len(result) > 2500:
                await event.edit(msg+"\n\n"+"__"+"Result is too big .. send as file__")
                with open("output.txt", "w+") as f:
                    f.write(result)
                await client.send_file(event.chat_id, 'output.txt')
                os.remove("output.txt")
            else:
                try:
                    if os.environ.get("sender_id")==str(event.sender_id):
                        await event.edit(msg+"\n\n"+"="*[20,max(len(result),12)][len(result)<20]+"\n"+"__OUTPUT:__\n\n**"+result+" **")
                    else:
                        await event.reply("** "+result+" **")
                except Exception as excp:
                    if os.environ.get("sender_id")==str(event.sender_id):
                        await event.edit(msg+"\n\n"+"="*[20,max(len(str(excp)),12)][len(str(excp))<20]+"\n"+"__ERROR:__\n\n**"+str(excp)+" **")
                    else:
                        await event.reply("** "+str(excp)+" **")
        except Exception as excp:
            if os.environ.get("sender_id")==str(event.sender_id):
                await event.edit(msg+"\n\n"+"="*[20,max(len(str(excp)),12)][len(str(excp))<20]+"\n"+"__PAGE ERROR:__\n\n**"+str(excp)+" **")
            else:
                await event.reply("** "+str(excp)+" **")
            
            
    @client.on(events.NewMessage(pattern="/gitrepo"))
    async def git_user_repo_info(event):
        msg = event.message.message
        try:
            
            await event.edit(msg+"\n\n"+"__"+"Running Git Repo Command . . ."+"__")
            try:
                code = msg.lstrip('/gitrepo')
            except IndexError:
                await event.edit(msg+"\n\n"+"__"+"No arguments given (gitrepo) ...__")
            command = "".join(f"\n {x}" for x in code.split("\n.strip()"))
            user_repo = command.strip()
            
            url = "https://github.com/"

            page = urllib.request.urlopen(url+user_repo)

            soup = BeautifulSoup(page,"html.parser")

            result = []
            result.append("Username: "+user_repo.split('/')[0])
            result.append("Repository: "+user_repo.split('/')[1])

            no_of_stars,no_of_forks,zip_link,no_of_watch,no_of_branches,no_of_issues = None,None,None,None,None,None
            
            try:
                no_of_stars = soup.find('a',{'href':'/'+user_repo+'/stargazers'}).text.strip()
                result.append("Number of stars: "+no_of_stars)
            except:
                pass
            try:
                no_of_forks = soup.find('a',{'href':'/'+user_repo+'/network/members'}).text.strip()
                result.append("Number of forks: "+no_of_forks)
            except:
                pass
            try:
                no_of_issues = soup.find('a',{'href':'/'+user_repo+'/issues'}).text.strip()
                result.append("Number of issues: "+no_of_issues.split("\n")[1].strip())
            except:
                pass
            try:
                zip_link = soup.find('a',{'href':'/'+user_repo+'/archive/master.zip'})['href']
                result.append("Zip link: "+url+zip_link)
            except:
                pass
            try:
                no_of_watch = soup.find('a',{'href':'/'+user_repo+'/watchers'}).text.strip()
                result.append("Watch: "+no_of_watch)
            except:
                pass
            try:
                no_of_branches = soup.find('a',{'href':'/'+user_repo+'/branches'}).text.strip()
                result.append("Number of Branches: "+no_of_branches.split("\n")[0].strip())
            except:
                pass
            # print(result)

            result = "\n".join(result)


#             print(result)
            if len(result) > 2500:
                await event.edit(msg+"\n\n"+"__"+"Result is too big .. send as file__")
                with open("output.txt", "w+") as f:
                    f.write(result)
                await client.send_file(event.chat_id, 'output.txt')
                os.remove("output.txt")
            else:
                try:
                    if os.environ.get("sender_id")==str(event.sender_id):
                        await event.edit(msg+"\n\n"+"="*[20,max(len(result),12)][len(result)<20]+"\n"+"__OUTPUT:__\n\n**"+result+" **")
                    else:
                        await event.reply("** "+result+" **")
                except Exception as excp:
                    if os.environ.get("sender_id")==str(event.sender_id):
                        await event.edit(msg+"\n\n"+"="*[20,max(len(str(excp)),12)][len(str(excp))<20]+"\n"+"__ERROR:__\n\n**"+str(excp)+" **")
                    else:
                        await event.reply("** "+str(excp)+" **")
        except Exception as excp:
            if os.environ.get("sender_id")==str(event.sender_id):
                await event.edit(msg+"\n\n"+"="*[20,max(len(str(excp)),12)][len(str(excp))<20]+"\n"+"__PAGE ERROR:__\n\n**"+str(excp)+" **")
            else:
                await event.reply("** "+str(excp)+" **")


    client.run_until_disconnected()

if __name__ == "__main__":
    config = {
        "api_id": os.environ.get("api_id"),
        "api_hash": os.environ.get("api_hash"),
        "session_name": os.environ.get("session_name"),
    }

    start(config)
