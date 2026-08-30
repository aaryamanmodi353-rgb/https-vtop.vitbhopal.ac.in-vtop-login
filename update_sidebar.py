import sys
import re

files = ["index.html", "profile.html", "credentials.html"]

sidebar_html = """        <aside class="sidebar" id="sidebar">
            <div class="sidebar-item">
                <button class="sidebar-icon"><i class="fa-solid fa-phone"></i></button>
                <div class="popup-menu" style="min-width: 150px; padding:0;">
                    <div class="popup-item" style="padding: 10px 20px;"><i class="fa-solid fa-phone"
                            style="font-size:12px; margin-right: 5px"></i> Contact Us</div>
                </div>
            </div>
            <div class="sidebar-item">
                <button class="sidebar-icon"><i class="fa-solid fa-briefcase"></i></button>
                <div class="popup-menu">
                    <div class="popup-title">My Info</div>
                    <a href="profile.html" class="popup-item" style="text-decoration:none; color:inherit; display:block;"><i class="fa-regular fa-circle-dot"></i> Profile</a>
                    <a href="credentials.html" class="popup-item" style="text-decoration:none; color:inherit; display:block;"><i class="fa-regular fa-circle-dot"></i> Credentials</a>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Acknowledgement View</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Student Bank Info</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> AAPAR ID Upload</div>
                </div>
            </div>
            <div class="sidebar-item">
                <button class="sidebar-icon"><i class="fa-solid fa-circle-info"></i></button>
                <div class="popup-menu">
                    <div class="popup-title">Info Corner</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> FAQ</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Spotlight</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> General</div>
                </div>
            </div>
            <div class="sidebar-item">
                <button class="sidebar-icon"><i class="fa-solid fa-paw"></i></button>
                <div class="popup-menu">
                    <div class="popup-title">Proctor</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Proctor Details</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Proctor Message</div>
                </div>
            </div>
            <div class="sidebar-item">
                <button class="sidebar-icon"><i class="fa-solid fa-graduation-cap"></i></button>
                <div class="popup-menu">
                    <div class="popup-title">Academics</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Faculty Info</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Class Messages</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> My Curriculum</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Time Table</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Class Attendance</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Course Page</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> QCM View</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Academics Calendar</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Course Withdraw</div>
                </div>
            </div>
            <div class="sidebar-item">
                <button class="sidebar-icon"><i class="fa-solid fa-building-columns"></i></button>
                <div class="popup-menu">
                    <div class="popup-title">Research</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> My Research Profile</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Course Work Registration</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Registration Status</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Meeting info</div>
                </div>
            </div>
            <div class="sidebar-item">
                <button class="sidebar-icon"><i class="fa-solid fa-book"></i></button>
                <div class="popup-menu">
                    <div class="popup-title">Examination</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Exam Schedule</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Online Exam Schedule</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Offline Exam Schedule</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Marks</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Grades</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Paper See/Rev</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Grade History</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Arrear/ReFAT Details</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Re-Exam Application</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Supplementry Registration</div>
                </div>
            </div>
            <div class="sidebar-item">
                <button class="sidebar-icon"><i class="fa-solid fa-space-shuttle"></i></button>
                <div class="popup-menu">
                    <div class="popup-title">Services</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> PAT Registration</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Transcript Request</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Late Hour Request</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Water Facility</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Transport Facility</div>
                </div>
            </div>
            <div class="sidebar-item">
                <button class="sidebar-icon"><i class="fa-solid fa-certificate"></i></button>
                <div class="popup-menu">
                    <div class="popup-title">Bonafide</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Apply Bonafide</div>
                </div>
            </div>
            <div class="sidebar-item">
                <button class="sidebar-icon"><i class="fa-solid fa-money-bill"></i></button>
                <div class="popup-menu">
                    <div class="popup-title">Online Payments</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Payments</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Payment Receipts</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Fees Intimation</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Hostel Fees Intimation</div>
                </div>
            </div>
            <div class="sidebar-item">
                <button class="sidebar-icon"><i class="fa-solid fa-house"></i></button>
                <div class="popup-menu">
                    <div class="popup-title">Hostels</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Leave Request</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Leave History</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Biometric Report</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Hostel Room Allotment</div>
                </div>
            </div>
            <div class="sidebar-item">
                <button class="sidebar-icon"><i class="fa-solid fa-trophy"></i></button>
                <div class="popup-menu">
                    <div class="popup-title">SW Events</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Event Requisition</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Event Attendance</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Event Registration</div>
                </div>
            </div>
            <div class="sidebar-item">
                <button class="sidebar-icon"><i class="fa-solid fa-lock"></i></button>
                <div class="popup-menu">
                    <div class="popup-title">My Account</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Backup Codes</div>
                    <div class="popup-item"><i class="fa-regular fa-circle-dot"></i> Change Password</div>
                </div>
            </div>
        </aside>"""

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # regex to find <aside class="sidebar" id="sidebar"> ... </aside>
    new_content = re.sub(r' *<aside class="sidebar" id="sidebar">.*?</aside>', sidebar_html, content, flags=re.DOTALL)
    
    with open(file, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated {file}")
