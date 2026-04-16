from os import environ
from dotenv import load_dotenv
from todoist_api_python.api import TodoistAPI
import wx
from wx.html import HtmlEasyPrinting
from datetime import date

load_dotenv()

app = wx.App()

api = TodoistAPI(environ.get("TODO_API"))

tasks = api.filter_tasks(query="@new")

for list in tasks:
    for task in list:
        todos = f"""
        <h1>{task.content}</h1>
        <p>
            <b>DAT:</b> {date.today()}<br>
            <b>TID:</b> {task.id}<br>
            <b>DES:</b> {task.description}<br>
            <b>PRI:</b> {task.priority}<br>
            <b>LAB:</b> {", ".join(task.labels)}<br>
            <b>PAR:</b> {task.parent_id}
        </p>
        """
        printer = HtmlEasyPrinting()
        printer.SetStandardFonts(size=+30) # this may only be needed in linux...
        printer.GetPageSetupData().SetMarginBottomRight(wx.Point(2, 2))
        printer.GetPageSetupData().SetMarginTopLeft(wx.Point(2, 2))
        printer.GetPageSetupData().SetPaperSize(wx.Size(80, 80))
        printer.SetPromptMode(HtmlEasyPrinting.Prompt_Never)
        printer.PrintText(todos)
        app.MainLoop()

api.remove_shared_label("new")