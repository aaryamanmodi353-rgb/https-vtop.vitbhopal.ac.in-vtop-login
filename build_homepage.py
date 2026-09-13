import re
import os

css = """
/* Homepage Styles */
.homepage-grid {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 15px;
    padding: 10px;
}
.home-card {
    background: white;
    border: 1px solid #ccc;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
}
.home-card-header {
    padding: 8px 12px;
    font-size: 11px;
    font-weight: bold;
    color: #333;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.border-bottom-blue {
    border-bottom: 2px solid #6fa8dc;
}
.badge-light {
    background: #fdf5e6;
    color: #cc0000;
    padding: 2px 10px;
    font-weight: bold;
    border-radius: 3px;
}
.home-card-body {
    padding: 10px;
}
.p-0 {
    padding: 0 !important;
}
.mt-3 {
    margin-top: 15px;
}
.home-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 10px;
    font-weight: 500;
}
.home-table th, .home-table td {
    padding: 6px 10px;
    text-align: left;
}
.home-table th {
    font-weight: bold;
    background: #fff;
    border-bottom: 1px solid #ddd;
}
.text-blue { color: #0b5394; }
.italic { font-style: italic; font-weight: bold;}
.text-red { color: #cc0000; }
.text-center { text-align: center !important; font-weight: bold;}
.bg-light-blue1 { background-color: #e6f2ff; width: 80px;}
.bg-light-blue2 { background-color: #b3d9ff; }
.bg-blue-primary { background-color: #4a86e8; }
.text-white { color: white; }
.home-table.no-border th, .home-table.no-border td {
    border: 1px solid #fff;
    border-bottom: 1px solid #f0f0f0;
    padding: 6px 10px;
}
"""

html = """<main class="content-area" style="background-color: #eef2f5;">
    <div class="homepage-grid">
        <div class="homepage-left">
            <!-- CURRENT SEMESTER COURSE REGISTRATION DETAILS -->
            <div class="home-card">
                <div class="home-card-header">
                    <span>CURRENT SEMESTER COURSE REGISTRATION DETAILS</span>
                    <span class="badge-light">FALLSEM2026-27</span>
                </div>
                <div class="home-card-body p-0">
                    <table class="home-table">
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>Code - Course Name</th>
                                <th>Type</th>
                                <th>Attendance</th>
                                <th>Remarks</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>1</td>
                                <td>DSN2093 - SEMESTER INTERNSHIP</td>
                                <td class="text-blue italic">PJ</td>
                                <td class="text-red">0.0</td>
                                <td class="text-red">Critical - must improve</td>
                            </tr>
                            <tr>
                                <td>2</td>
                                <td>DSN4091 - Capstone Project - Phase 1</td>
                                <td class="text-blue italic">PJ</td>
                                <td class="text-red">0.0</td>
                                <td class="text-red">Critical - must improve</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- SPOT-LIGHT -->
            <div class="home-card mt-3">
                <div class="home-card-header border-bottom-blue">
                    <span>SPOT-LIGHT</span>
                </div>
                <div class="home-card-body" style="height: 500px;">
                </div>
            </div>
        </div>

        <div class="homepage-right">
            <!-- PROCTOR Message -->
            <div class="home-card">
                <div class="home-card-header border-bottom-blue">
                    <span>PROCTOR Message</span>
                </div>
                <div class="home-card-body" style="height: 60px;">
                </div>
            </div>

            <!-- CGPA and CREDIT Status -->
            <div class="home-card mt-3">
                <div class="home-card-header border-bottom-blue">
                    <span>CGPA and CREDIT Status</span>
                </div>
                <div class="home-card-body p-0">
                    <table class="home-table no-border">
                        <tbody>
                            <tr>
                                <td>Total Credits Required :</td>
                                <td class="bg-light-blue1 text-center">189</td>
                            </tr>
                            <tr>
                                <td>Earned Credits :</td>
                                <td class="bg-light-blue2 text-center">160.0</td>
                            </tr>
                            <tr>
                                <td>Current CGPA :</td>
                                <td class="bg-blue-primary text-white text-center">8.79</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</main>"""

index_path = "index.html"
css_path = "styles.css"

if os.path.exists(css_path):
    with open(css_path, "a", encoding="utf-8") as f:
        f.write(css)

if os.path.exists(index_path):
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = re.sub(r'<main class="content-area">.*?</main>', html, content, flags=re.DOTALL)

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(new_content)

print("Done building homepage")
