import re
import os

new_css = '''/* Homepage Styles */
.homepage-grid {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 15px;
    padding: 10px;
    background-color: #eef2f5;
}
.home-card {
    background: white;
    border: 1px solid #d3d3d3;
    border-top: 3px solid #5b9bd5;
    box-shadow: none;
}
.home-card-header {
    padding: 8px 12px;
    font-size: 11px;
    color: #000;
    border-bottom: 1px solid #e0e0e0;
}
.header-with-badge {
    display: flex;
    align-items: center;
}
.header-title {
    margin-right: auto;
}
.badge-light {
    background: #fdf2e9;
    color: #c00000;
    padding: 4px 0;
    width: 40%;
    text-align: center;
    font-size: 10px;
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
}
.home-table th, .home-table td {
    padding: 8px 10px;
    text-align: center;
    border-bottom: 1px solid #f0f0f0;
}
.home-table th:nth-child(2), .home-table td:nth-child(2) {
    text-align: left;
}
.home-table th {
    font-weight: normal;
    color: #000;
    background: #fff;
    border-bottom: 2px solid #e0e0e0;
}
.text-blue { color: #0056b3; }
.italic { font-style: italic; }
.text-red { color: #c00000; }
.bg-light-blue1 { background-color: #e8f0fe; width: 80px;}
.bg-light-blue2 { background-color: #a4c2f4; }
.bg-blue-primary { background-color: #4285f4; }
.text-white { color: white; }
.home-table.no-border th, .home-table.no-border td {
    border: 1px solid #e0e0e0;
    border-top: none;
    border-bottom: 1px solid #e0e0e0;
    padding: 6px 10px;
    text-align: left;
}
.home-table.no-border td:last-child {
    text-align: center;
}
.spotlight-container {
    margin-top: 15px;
}
.spotlight-text {
    font-size: 12px;
    color: #000;
    display: inline-block;
    border-bottom: 2px solid #5b9bd5;
    padding-bottom: 5px;
    width: 40%;
}
'''

new_html = '''<main class="content-area" style="background-color: #eef2f5;">
    <div class="homepage-grid">
        <div class="homepage-left">
            <!-- CURRENT SEMESTER COURSE REGISTRATION DETAILS -->
            <div class="home-card">
                <div class="home-card-header header-with-badge p-0" style="padding:0;">
                    <div style="padding: 8px 12px;" class="header-title">CURRENT SEMESTER COURSE REGISTRATION DETAILS</div>
                    <div class="badge-light">FALLSEM2026-27</div>
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
            <div class="spotlight-container">
                <div class="spotlight-text">SPOT-LIGHT</div>
            </div>
        </div>

        <div class="homepage-right">
            <!-- PROCTOR Message -->
            <div class="home-card">
                <div class="home-card-header">
                    <span>PROCTOR Message</span>
                </div>
                <div class="home-card-body" style="height: 80px;">
                </div>
            </div>

            <!-- CGPA and CREDIT Status -->
            <div class="home-card mt-3">
                <div class="home-card-header">
                    <span>CGPA and CREDIT Status</span>
                </div>
                <div class="home-card-body p-0">
                    <table class="home-table no-border">
                        <tbody>
                            <tr>
                                <td>Total Credits Required :</td>
                                <td class="bg-light-blue1">189</td>
                            </tr>
                            <tr>
                                <td>Earned Credits :</td>
                                <td class="bg-light-blue2">160.0</td>
                            </tr>
                            <tr>
                                <td>Current CGPA :</td>
                                <td class="bg-blue-primary text-white">8.79</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</main>'''

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
new_content = re.sub(r'<main class="content-area".*?</main>', new_html, content, flags=re.DOTALL)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

# 2. Update styles.css
with open('styles.css', 'r', encoding='utf-8') as f:
    css_content = f.read()
css_content = re.sub(r'/\* Homepage Styles \*/.*', new_css, css_content, flags=re.DOTALL)
with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print('Adjusted styles and HTML to perfectly match the screenshot.')
