# Automated_Optimizer
<p align="center">
<img src='http://s7.postimg.org/kcbprgjqj/Untitled.png'><br>
</p>
A Tkinter GUI for quickly running basic optimization/cleanup programs. It's still a work in progress but the premise is to combine several powerful opensource/freeware tools into <b>one</b> location. Make that software conveniently executable by cutting down on overall clicks, window navigation and HID swapping. While maintaining the utmost concern for portability, offline access and minimalism to performance ratio. The top priorities when tasked with repairing systems/setups that are always changing.

Intended to be used by computer repair technicians that use a select number of tools and services to perform a repetative series of repairs. Ultimately, resulting in saving countless labor hours over time and faster turn around time for clients. Furthermore cutting down overall client costs when hiring a Tech for onsite (by the hour) projects.

It will be later expanded to include other projects like my Hardware tester, Auto Listing process, Diagnostic/Repair progs, I'm considering even a possible Symbaloo style GUI + Portable Firefox (Adblock, Selenium, LastPass...) Combo.

<u>Example of My Current process:</u>

Having an 'offline' library of known portable progs organized into individual folders, on a Jump Drive. <br>
* `Win+E` (My Computer), `double click` external USB.
* `doubleclick` the specific prog folder<br>
* `doubleclick` the executable to load the desired prog.<br>
* `exit` prog, `back` in the folder directory.
* `double click` secondary diagnostic prog folder
* `double click` executable
* then rinse and repeat for each additional task. <br>
[12 clicks + 2 keystrokes + 4 Window/Directory Changes]

<u>Compared to what this repo offers:</u><br>

* `Win+E` > `Double Click` Jump Drive
* `double click` Main .Py/.EXE script.
* `single click` desired diagnostic prog.
* `exit` (no need to `back` out of the directory)
* `single click` secondary diag prog.<br>
[7 clicks + 2 Keystrokes + 2 Window/Directory Changes + Consolidates HID swapping]

It's worth mentioning that if AutOptimizer is burned to a CD (B.L.D.Z.R compat. implied) then a simple `autorun.inf` file will subtract 4 clicks and 2 keystrokes.
