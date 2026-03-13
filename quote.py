import zenquotespy
import wx
from wx.html import HtmlEasyPrinting
from datetime import date

app = wx.App()

quote = f"""
    <p>Quote of the day for {date.today()}</p>
    <h1>{zenquotespy.random()}</h1>"""

printer = HtmlEasyPrinting()
printer.GetPageSetupData().SetMarginBottomRight(wx.Point(2, 2))
printer.GetPageSetupData().SetMarginTopLeft(wx.Point(2, 2))
printer.GetPageSetupData().SetPaperSize(wx.Size(80, 80))
printer.SetPromptMode(HtmlEasyPrinting.Prompt_Never)
printer.PrintText(quote)