import qrcode

link = "https://github.com/gundeep548-cmd/student_attendance_project.git"

qr = qrcode.make(link)

qr.save("project_qr.png")

print("QR Code Generally Successfully")