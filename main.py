from os import environ
from dotenv import load_dotenv
from todoist_api_python.api import TodoistAPI
import wx
from wx.html import HtmlEasyPrinting

load_dotenv()

app = wx.App()

api = TodoistAPI(environ.get("TODO_API"))

tasks = api.filter_tasks(query="today")

for list in tasks:
    for task in list:
        todos = f"""
        <h1>{task.content}</h1>
        <p>
            TID: {task.id}<br>
            DES: {task.description}<br>
            PRI: {task.priority}<br>
            LAB: {task.labels}<br>
            PAR: {task.parent_id}
        </p>
        """
        printer = HtmlEasyPrinting()
        printer.GetPageSetupData().SetMarginBottomRight(wx.Point(2, 2))
        printer.GetPageSetupData().SetMarginTopLeft(wx.Point(2, 2))
        printer.GetPageSetupData().SetPaperSize(wx.Size(80, 80))
        printer.SetPromptMode(HtmlEasyPrinting.Prompt_Never)
        printer.PrintText(todos)
        app.MainLoop()