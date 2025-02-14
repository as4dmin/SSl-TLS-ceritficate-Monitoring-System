
## **🔐 SSL/TLS Certificate Monitor**
A Python script to **monitor SSL/TLS certificates**, check their expiration dates, and send alerts via **email notifications** when a certificate is about to expire.

---

## **🚀 Features**
- ✅ **Check SSL/TLS Certificate Expiry**
- ✅ **Validate Domain Names & Email Addresses**
- ✅ **Fetch SSL/TLS Certificates Securely**
- ✅ **Send Email Alerts for Expiring Certificates**
- ✅ **Logging Support** (stores logs in `ssl_monitor.log`)

---

## **📌 Requirements**
### **1. Install Python Dependencies**
Ensure you have Python **3.6+** installed.

Install required dependencies:
```bash
pip install -r requirements.txt
```

### **2. Set Up Email Notifications**
To send email alerts, you need to set up **Gmail SMTP** authentication.

#### **🔹 Enable App Passwords (For Gmail Users)**
1. Go to **Google Account Security** → [Click Here](https://myaccount.google.com/security).
2. Enable **2-Step Verification**.
3. Generate an **App Password**.
4. Copy the generated **App Password** (16-character code).
5. Set the credentials as environment variables (see below).

### **3. Set Environment Variables**
To securely store your email credentials, run the following:

#### **🔹 Linux/macOS (Bash Terminal)**
```bash
export EMAIL_USER="your-email@gmail.com"
export EMAIL_PASS="your-app-password"
```

#### **🔹 Windows (Command Prompt)**
```cmd
set EMAIL_USER=your-email@gmail.com
set EMAIL_PASS=your-app-password
```

#### **🔹 Windows (PowerShell)**
```powershell
$env:EMAIL_USER="your-email@gmail.com"
$env:EMAIL_PASS="your-app-password"
```

---

## **📌 How to Use**
1. **Run the Script**
   ```bash
   python ssl-monitor.py
   ```
2. Enter a domain (e.g., `google.com`).
3. If the SSL certificate is **expiring within 30 days**, enter an email to receive an alert.
4. To exit, type `exit`.

---

## **📄 Example Usage**
```
Enter domain (or 'exit' to quit): google.com
[INFO] SSL certificate for google.com is valid. Expires in 65 days.

Enter domain (or 'exit' to quit): facebook.com
[WARNING] SSL certificate for facebook.com is expiring in 7 days!
Enter recipient email: example@domain.com
[INFO] Email notification sent.
```

---

## **🛠 File Structure**
```
📁 SSL-Certificate-Monitor
│── 📄 ssl-monitor.py       # Main script
│── 📄 requirements.txt     # Python dependencies
│── 📄 README.md            # Project documentation
│── 📄 ssl_monitor.log      # Log file (created when the script runs)
```

---

## **📜 License**
This project is licensed under the **MIT License**. You are free to use and modify it.

---

## **🤝 Contributing**
If you want to contribute:
1. Fork the repository.
2. Create a new branch:  
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:  
   ```bash
   git commit -m "Added a new feature"
   ```
4. Push to GitHub:  
   ```bash
   git push origin feature-branch
   ```
5. Submit a Pull Request.

---

## **📞 Support**
For any issues or suggestions, open an **issue** in the GitHub repository.

---

### **🌟 If you find this useful, consider giving a ⭐ on GitHub! 🚀**
---

## **📥 Clone Repository**
To clone this project:
```bash
git clone https://github.com/yourusername/SSL-Certificate-Monitor.git
cd SSL-Certificate-Monitor
```

---

✅ **Now you are ready to upload this to GitHub!** 🚀  
Let me know if you need any changes! 😊
