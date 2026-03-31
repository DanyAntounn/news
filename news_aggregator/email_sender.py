"""
Module to send news articles via email
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict
import os
from dotenv import load_dotenv
from datetime import datetime


class EmailSender:
    """Sends formatted news articles via email"""
    
    def __init__(self, sender_email: str = None, sender_password: str = None):
        """
        Initialize email sender with Gmail account
        
        Args:
            sender_email: Gmail address
            sender_password: Gmail app password (NOT regular password)
        """
        load_dotenv()
        self.sender_email = sender_email or os.getenv('SENDER_EMAIL')
        self.sender_password = sender_password or os.getenv('SENDER_PASSWORD')
        self.smtp_server = 'smtp.gmail.com'
        self.smtp_port = 587
        
        if not self.sender_email or not self.sender_password:
            raise ValueError("Email credentials not found in environment variables")
    
    def format_articles_html(self, articles: List[Dict], topic: str = '') -> str:
        """
        Format articles as HTML email
        
        Args:
            articles: List of article dictionaries
            topic: News topic
        
        Returns:
            HTML string
        """
        timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")
        
        html = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    margin: 0;
                    padding: 20px;
                }}
                .container {{
                    background-color: white;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 30px;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }}
                .header {{
                    border-bottom: 3px solid #0066cc;
                    padding-bottom: 15px;
                    margin-bottom: 25px;
                }}
                .header h1 {{
                    color: #0066cc;
                    margin: 0;
                    font-size: 28px;
                }}
                .header p {{
                    color: #666;
                    margin: 10px 0 0 0;
                    font-size: 14px;
                }}
                .article {{
                    border-left: 4px solid #0066cc;
                    padding-left: 15px;
                    margin-bottom: 25px;
                    padding-bottom: 20px;
                    border-bottom: 1px solid #eee;
                }}
                .article:last-child {{
                    border-bottom: none;
                }}
                .article h2 {{
                    color: #0066cc;
                    margin: 0 0 10px 0;
                    font-size: 18px;
                    line-height: 1.4;
                }}
                .article h2 a {{
                    color: #0066cc;
                    text-decoration: none;
                }}
                .article h2 a:hover {{
                    text-decoration: underline;
                }}
                .source {{
                    color: #999;
                    font-size: 12px;
                    margin-bottom: 8px;
                }}
                .summary {{
                    color: #333;
                    font-size: 14px;
                    line-height: 1.6;
                    margin-bottom: 10px;
                }}
                .read-more {{
                    display: inline-block;
                    background-color: #0066cc;
                    color: white;
                    padding: 8px 16px;
                    text-decoration: none;
                    border-radius: 4px;
                    font-size: 13px;
                }}
                .read-more:hover {{
                    background-color: #0052a3;
                }}
                .footer {{
                    background-color: #f9f9f9;
                    padding: 15px;
                    border-radius: 4px;
                    margin-top: 25px;
                    color: #666;
                    font-size: 12px;
                    text-align: center;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>📰 Daily News Digest</h1>
                    <p>Topic: <strong>{topic}</strong> | {timestamp}</p>
                </div>
        """
        
        if not articles:
            html += "<p style='color: #999;'>No articles found for your topic.</p>"
        else:
            for article in articles:
                html += f"""
                <div class="article">
                    <div class="source">{article.get('source', 'Unknown')} • {article.get('published_at', 'Unknown')}</div>
                    <h2><a href="{article.get('url', '#')}">{article.get('title', 'N/A')}</a></h2>
                    <p class="summary">{article.get('summary', 'No summary available')}</p>
                    <a href="{article.get('url', '#')}" class="read-more">Read Full Article →</a>
                </div>
                """
        
        html += """
                <div class="footer">
                    <p>This is an automated news digest. You can change the topic or unsubscribe anytime.</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        return html
    
    def send_email(self, recipient_email: str, articles: List[Dict], 
                   topic: str = '', subject: str = None) -> bool:
        """
        Send news articles via email
        
        Args:
            recipient_email: Email address to send to
            articles: List of article dictionaries
            topic: News topic
            subject: Custom email subject (optional)
        
        Returns:
            True if successful, False otherwise
        """
        try:
            if not subject:
                subject = f"Daily News Digest - {topic}" if topic else "Daily News Digest"
            
            # Create message
            message = MIMEMultipart('alternative')
            message['Subject'] = subject
            message['From'] = self.sender_email
            message['To'] = recipient_email
            
            # Create HTML content
            html_content = self.format_articles_html(articles, topic)
            html_part = MIMEText(html_content, 'html')
            message.attach(html_part)
            
            # Send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(message)
            
            print(f"✓ Email sent successfully to {recipient_email}")
            return True
            
        except smtplib.SMTPAuthenticationError:
            print("✗ Authentication failed. Check your email and app password.")
            return False
        except smtplib.SMTPException as e:
            print(f"✗ SMTP Error: {e}")
            return False
        except Exception as e:
            print(f"✗ Error sending email: {e}")
            return False


if __name__ == '__main__':
    # Test email sender
    sample_articles = [
        {
            'title': 'Breaking News Title',
            'summary': 'This is a sample article summary that would appear in your email.',
            'url': 'https://example.com',
            'source': 'Example News',
            'published_at': '2 hours ago'
        }
    ]
    
    sender = EmailSender()
    sender.send_email('recipient@example.com', sample_articles, 'Test Topic')
