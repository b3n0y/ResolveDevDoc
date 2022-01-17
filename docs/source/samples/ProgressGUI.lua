_VERSION = [[Version 1.0 - November 18, 2017]]
--[[--
==============================================================================
ProgressGUI - v1.0 2017-11-18
==============================================================================
Fu Required: Fusion 9.0.1+
Created By : Andrew Hazelden[andrew@andrewhazelden]

==============================================================================
Overview
==============================================================================

This Lua script example creates a progress window using Fusion 9's UI Manager library.

I think the example is interesting because it shows how you can use two functions to interact with the window. One function creates the new window and returns pointers to the window, and to the win:GetItems() based controls in the view. Then the 2nd function allows you to update the view as you run through a loop in your script.

The two progress bar cell "on" and "off" image elements in the script were created from PNG images that were converted into base64 encoded strings. This was done using a technique presented by Dunn that was discussed on the "HTML Image Source Example" UI Manager post here:

https://www.steakunderwater.com/wesuckless/viewtopic.php?f=6&t=1411&p=10500#p10500

==============================================================================
Usage
==============================================================================

Step 1. Copy this script to the Fusion user prefs Scripts:/Comp folder.

Step 2. Run the script in Fusion by selecting the "Script > ProgressGUI" menu item.

--]]--


-- The Main function
function Main()
	-- Check if the Fusion GUI is running
	if fusion == nil then
		print("[Fusion] Error: Please open up the Fusion GUI before running this tool.\n")
	else
		-- Check what version of Fusion is active
		local fuVersion = math.floor(tonumber(eyeon._VERSION))
		if fuVersion < 9 then
			-- Fusion 7 or 8 was detected
			print("[UI Manager] Fusion 9.0.1 or higher is required. Detected Fusion " .. tostring(eyeon._VERSION) .. "\n")
		else
			-- Fusion 9+ is running

			-- Find out the current Fusion host platform (Windows/Mac/Linux)
			platform = (FuPLATFORM_WINDOWS and "Windows") or (FuPLATFORM_MAC and "Mac") or (FuPLATFORM_LINUX and "Linux")

			-- Display the progress dialog
			ui = app.UIManager
			disp = bmd.UIDispatcher(ui)

			-- Show the progress window
			local msgwin,msgitm = ProgressWinCreate()

			local progressTable = {
				"Creating a New Fusion Project...",
				"Downloading Cool Font Used in Behance Frontpage Artwork...",
				"Creating Procedural Node Based Animation...",
				"Searching for new iStock Soundtrack...",
				"Opening Google Image Search With Usage Rights Specified...",
				"Rendering Comp...",
				"Creating Movie Encode...",
				"Uploading Content to Customer...",
				"Sending Billing Message...",
				"Receiving Bitcoin Payment...",
				"Booking Plane Ticket to Island Paradise...",
			}

			-- How many steps does this task require
			totalSteps = 11

			-- Run the progress dialog updating cycle
			for step = 1, totalSteps do
				ProgressWinUpdate(msgwin, msgitm, "ProgressGUI Example", progressTable[step], step, totalSteps, 2)
			end

			-- Hide the progress window
			msgwin:Hide()
		end
	end
end

-- Progress Window Creation
-- Example: local msgwin,msgitm = ProgressWinCreate()
function ProgressWinCreate()

	local originX, originY, width, height = 450, 300, 540, 250

	local win = disp:AddWindow({
		ID = "MsgWin",
		WindowTitle = "",
		Target = "MsgWin",
		Geometry = {originX, originY, width, height},

		ui:VGroup{
			ui:Label{
				ID = "Title",
				Text = "",
				Alignment = {
					AlignHCenter = true,
					AlignVCenter = true,
				},
				Font = ui:Font{
					PixelSize = 18,
				},
				WordWrap = true,
			},

			ui:Label{
				ID = "Message",
				Text = "",
				Alignment = {
					AlignHCenter = true,
					AlignVCenter = true,
				},
				WordWrap = true,
			},

			ui:TextEdit{
				ID = "ProgressHTML",
				ReadOnly = true,
			},

		}
	})

	-- Add your GUI element based event functions here:
	itm = win:GetItems()

	win:Show()

	return win,itm
end


-- Progress Window Refresh
-- Example: ProgressWinUpdate(msgwin, msgitm, "Status Update", "Rendering Comp...", 1, 10, 1)
function ProgressWinUpdate(win, itm, title, text, progressLevel, progressMax, delaySeconds)
	-- Update the window title
	itm.MsgWin.WindowTitle = tostring(title)

	-- Update the heading Text
	itm.Title.Text = title .. "\nStep " ..  tostring(progressLevel) .. " of " .. tostring(progressMax)
	
	itm.Message.Text = text

	-- Print the error to the Console tab
	if comp ~= nil then
		comp:Print(text .. "\n")
	end

	-- Add the webpage header text
	html = "<html>\n"
	html = html .."\t<head>\n"
	html = html .."\t\t<style>\n"
	html = html .."\t\t</style>\n"
	html = html .."\t</head>\n"
	html = html .."\t<body>\n"
	html = html .. "\t\t<div>"
	html = html .. "\t\t\t<div style=\"float:right;width:46px;\">\n"

	-- progressScale is a multiplier to adjust to the progressMax range vs number of bar elements rendered onscreen
	progressScale = 5

	-- Scale the progress values to better fill the window size
	progressLevelScaled = progressLevel * progressScale
	progressMaxScaled = progressMax * progressScale

	-- Update the activity monitor view - Turn the images into HTML <img> tags
	for img = 1, progressLevelScaled do
		-- These images are the progressbar "ON" cells
		html = html .. ProgressbarCellON()
	end

	for img = progressLevelScaled + 1, progressMaxScaled do
		-- These images are the progressbar "OFF" cells
		html = html .. ProgressbarCellOFF()
	end

	html = html .. "\t\t\t</div>\n"
	html = html .. "\t\t</div>\n"
	html = html .. "\t</body>\n"
	html = html .. "</html>"

	-- Refresh the progress bar
	-- print("[HTML]\n" .. html)
	itm.ProgressHTML.HTML = html

	-- Pause to show the message
	bmd.wait(delaySeconds)
end


-- Progressbar ON cell encoded as Base64 content
-- Example: itm.Progress.HTML = ProgressbarCellON() 
function ProgressbarCellON()
	return [[<img src='data:image/png;base64,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'/>]]
end
	
-- Progressbar off cell encoded as Base64 content
-- Example: itm.Progress.HTML = ProgressbarCellOFF() 
function ProgressbarCellOFF()
	return [[<img src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAuCAIAAAB1WqTJAAABG2lUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4KPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNS41LjAiPgogPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIi8+CiA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgo8P3hwYWNrZXQgZW5kPSJyIj8+Gkqr6gAADB5pQ0NQRGlzcGxheQAASImlV3dYU8kWn1tSCAktEAEpoTdBepXei4B0EJWQBAglhISgYkcWFVwLKqJY0VURFdcCyFoRu4uAvS6IqKysiwUbKm9SQNf93vvnne+bmV/OnHPmd+aeezMDgLJPLjtPhKoAkMcvFMYE+zGTklOYpB5ABrpAGTgAVxZbJPCNjo4AUEbHf8q7WwCRjNetJbH+Pf8/RZXDFbEBQKIhLuSI2HkQtwGAa7IFwkIACA+g3mhmoQBiosReXQgJQqwuwZkybC7B6TI8SWoTF+MPMYxJprJYwkwAlFKhnlnEzoRxlOZCbMvn8PgQ74PYi53F4kA8APGEvLx8iJU1ITZP/y5O5j9ipo/FZLEyx7AsF6mQA3giQS5r9mieZBAAeEAEBCAXsMCY+v+XvFzx6JqGsFGzhCExkj2A+7gnJz9cgqkQH+enR0ZBrAbxRR5Hai/B97LEIfFy+wG2yB/uIWAAgAIOKyAcYh2IGeKceF85tmcJpb7QHo3kFYbGyXG6MD9GHh8t4udGRsjjLM3iho7iLVxRYOyoTQYvKBRiWHnokeKsuEQZT7StiJcQCbESxB2inNhwue+j4iz/yFEboThGwtkY4rcZwqAYmQ2mKa8+GB+zYbOka8HniPkUZsWFyHyxJK4oKWKUA4cbECjjgHG4/Hg5NwxWm1+M3LdMkBstt8e2cHODY2T7jB0UFcWO+nYVwoKT7QP2OJsVFi1f652gMDpOxg1HQQTwhzXABGLY0kE+yAa89oGmAfhLNhME60IIMgEXWMs1ox6J0hk+7GNBMfgLIi6spFE/P+ksFxRB/Zcxray3BhnS2SKpRw54CnEero174R54BOx9YLPHXXG3UT+m8uiqxEBiADGEGES0GOPBhqxzYRPCSv63LhyOXJidhAt/NIdv8QhPCZ2Ex4SbhG7CXZAAnkijyK1m8EqEPzBngsmgG0YLkmeX/n12uClk7YT74Z6QP+SOM3BtYI07wkx8cW+YmxPUfs9QPMbt217+uJ6E9ff5yPVKlkpOchbpY0/Gf8zqxyj+3+0RB47hP1piS7HD2AXsDHYJO441ASZ2CmvGrmInJHisEp5IK2F0tRgptxwYhzdqY1tv22/7+Ye1WfL1JfslKuTOKpS8DP75gtlCXmZWIdNXIMjlMkP5bJsJTHtbOxcAJN962afjDUP6DUcYl7/pCk4D4FYOlZnfdCwjAI49BYD+7pvO6DUs91UAnOhgi4VFMh0u6QiAAv9D1IEW0ANGwBzmYw+cgQfwAYEgDESBOJAMpsMdzwJ5kPNMMBcsAmWgAqwC68BGsBXsAHvAfnAINIHj4Aw4D66ADnAT3Id10QdegEHwDgwjCEJCaAgd0UL0ERPECrFHXBEvJBCJQGKQZCQNyUT4iBiZiyxGKpBKZCOyHalDfkWOIWeQS0gnchfpQfqR18gnFEOpqDqqi5qiE1FX1BcNR+PQaWgmWoAWo6XoCrQarUX3oY3oGfQKehPtRl+gQxjAFDEGZoBZY66YPxaFpWAZmBCbj5VjVVgtdgBrgc/5OtaNDWAfcSJOx5m4NazNEDweZ+MF+Hx8Ob4R34M34m34dbwHH8S/EmgEHYIVwZ0QSkgiZBJmEsoIVYRdhKOEc/C96SO8IxKJDKIZ0QW+l8nEbOIc4nLiZmID8TSxk9hLHCKRSFokK5InKYrEIhWSykgbSPtIp0hdpD7SB7IiWZ9sTw4ip5D55BJyFXkv+SS5i/yMPKygomCi4K4QpcBRmK2wUmGnQovCNYU+hWGKKsWM4kmJo2RTFlGqKQco5ygPKG8UFRUNFd0UpyjyFBcqViseVLyo2KP4kapGtaT6U1OpYuoK6m7qaepd6hsajWZK86Gl0AppK2h1tLO0R7QPSnQlG6VQJY7SAqUapUalLqWXygrKJsq+ytOVi5WrlA8rX1MeUFFQMVXxV2GpzFepUTmmcltlSJWuaqcapZqnulx1r+ol1edqJDVTtUA1jlqp2g61s2q9dIxuRPens+mL6Tvp5+h96kR1M/VQ9Wz1CvX96u3qgxpqGo4aCRqzNGo0Tmh0MzCGKSOUkctYyTjEuMX4NE53nO847rhl4w6M6xr3XnO8po8mV7Ncs0HzpuYnLaZWoFaO1mqtJq2H2ri2pfYU7ZnaW7TPaQ+MVx/vMZ49vnz8ofH3dFAdS50YnTk6O3Su6gzp6ukG6wp0N+ie1R3QY+j56GXrrdU7qdevT9f30ufpr9U/pf8nU4Ppy8xlVjPbmIMGOgYhBmKD7QbtBsOGZobxhiWGDYYPjShGrkYZRmuNWo0GjfWNJxvPNa43vmeiYOJqkmWy3uSCyXtTM9NE0yWmTabPzTTNQs2KzerNHpjTzL3NC8xrzW9YEC1cLXIsNlt0WKKWTpZZljWW16xQK2crntVmq84JhAluE/gTaifctqZa+1oXWddb99gwbCJsSmyabF5ONJ6YMnH1xAsTv9o62eba7rS9b6dmF2ZXYtdi99re0p5tX2N/w4HmEOSwwKHZ4ZWjlSPXcYvjHSe602SnJU6tTl+cXZyFzgec+12MXdJcNrncdlV3jXZd7nrRjeDm57bA7bjbR3dn90L3Q+5/e1h75Hjs9Xg+yWwSd9LOSb2ehp4sz+2e3V5MrzSvbV7d3gbeLO9a78c+Rj4cn10+z3wtfLN99/m+9LP1E/od9Xvv7+4/z/90ABYQHFAe0B6oFhgfuDHwUZBhUGZQfdBgsFPwnODTIYSQ8JDVIbdDdUPZoXWhg2EuYfPC2sKp4bHhG8MfR1hGCCNaJqOTwyavmfwg0iSSH9kUBaJCo9ZEPYw2iy6I/m0KcUr0lJopT2PsYubGXIilx86I3Rv7Ls4vbmXc/XjzeHF8a4JyQmpCXcL7xIDEysTupIlJ85KuJGsn85KbU0gpCSm7UoamBk5dN7Uv1Sm1LPXWNLNps6Zdmq49PXf6iRnKM1gzDqcR0hLT9qZ9ZkWxallD6aHpm9IH2f7s9ewXHB/OWk4/15NbyX2W4ZlRmfE80zNzTWZ/lndWVdYAz5+3kfcqOyR7a/b7nKic3TkjuYm5DXnkvLS8Y3w1fg6/LV8vf1Z+p8BKUCboLnAvWFcwKAwX7hIhommi5kJ1eMy5KjYX/yTuKfIqqin6MDNh5uFZqrP4s67Otpy9bPaz4qDiX+bgc9hzWucazF00t2ee77zt85H56fNbFxgtKF3QtzB44Z5FlEU5i34vsS2pLHm7OHFxS6lu6cLS3p+Cf6ovUyoTlt1e4rFk61J8KW9p+zKHZRuWfS3nlF+usK2oqvi8nL388s92P1f/PLIiY0X7SueVW1YRV/FX3VrtvXpPpWplcWXvmslrGtcy15avfbtuxrpLVY5VW9dT1ovXd1dHVDdvMN6wasPnjVkbb9b41TRs0tm0bNP7zZzNXVt8thzYqru1Yuunbbxtd7YHb2+sNa2t2kHcUbTj6c6EnRd+cf2lbpf2ropdX3bzd3fvidnTVudSV7dXZ+/KerReXN+/L3Vfx/6A/c0HrA9sb2A0VBwEB8UH//w17ddbh8IPtR52PXzgiMmRTUfpR8sbkcbZjYNNWU3dzcnNncfCjrW2eLQc/c3mt93HDY7XnNA4sfIk5WTpyZFTxaeGTgtOD5zJPNPbOqP1/tmkszfaprS1nws/d/F80PmzF3wvnLroefH4JfdLxy67Xm664nyl8arT1aO/O/1+tN25vfGay7XmDreOls5JnSe7vLvOXA+4fv5G6I0rNyNvdt6Kv3Xndurt7jucO8/v5t59da/o3vD9hQ8ID8ofqjyseqTzqPYPiz8aup27T/QE9Fx9HPv4fi+798UT0ZPPfaVPaU+rnuk/q3tu//x4f1B/x59T/+x7IXgxPFD2l+pfm16avzzyt8/fVweTBvteCV+NvF7+RuvN7reOb1uHoocevct7N/y+/IPWhz0fXT9e+JT46dnwzM+kz9VfLL60fA3/+mAkb2REwBKypEcBDDY0IwOA17sBoCXDs0MHABQl2V1MKojs/ihF4L9h2X1NKs4A7PYBIH4hABHwjLIFNhOIqXCUHL3jfADq4DDW5CLKcLCXxaLCGwzhw8jIG10ASC0AfBGOjAxvHhn5shOSvQvA6QLZHVAiRHi+32YjQR19L8GP8h+KMnBmRR2RSAAAAAlwSFlzAAAOxAAADsQBlSsOGwAAAeVJREFUOI1dU8tuFDEQrOrpzZJkWYWHEsEvcefnuXBAAoGiQJLNZHfsLg7tGU/SGtmy+1VV7uHXL9e7i+H8jZEgAPLDlX/7Pv74dfRP12fv9v525wDS/fnm7DDG3X3x/eXw/mqz3w0ASAK4+bjd78bthm7GYeDG2TzAxbn5QLP0GUAakU6zwQwAXFIIBCSsjGa0EBRKa9ccAEXI1+GhlpNHzy0jCC1HLf0yw1pNy1CTOopQS8zVWoUZi9QSkgOABaOaOpKU/aKXJQEOAhTyiI6eSrnZakYo1PqIlNCkAyzUuy2CZWcHEIEaIEGJBMmOc+ZAMulTM5UVN6EGwEFCRM+DBLLJMuNc4VheSYAkT8kbPzaULQ+SQmpO9NEA7BW1xNwlF+avPy0kWMLNFYDa/CT3Vy+02k3RXDMCSNH1xMvhlCIW7ilYj1BJYm0+EwgJstUEYEubFfxI5C81a+6Sca4c3taTC04AFoFXFvOVk72mQQBqFYBYNHuRp9XMp3H+izQ/t9dQjnYjB5Q6z8Tt3XR5PmzPzJ0bN7PewgGUqudj4AhabJzjMTLVQ4hQTc2kWvXwWB4PdXyuXopOk05TLLqMzzFNUar88FT/PZQ1h59/Tg+Heprkf++LgKexLr7B8Pt2KkX/ASixpbNlQGREAAAAAElFTkSuQmCC'/>]]
end


-- Run the main function
Main()