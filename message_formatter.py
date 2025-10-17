
import random

# Regular space for alignment
SPACE = ' '

# Rich crystal colors optimized for dark backgrounds
CRYSTAL_COLORS = [
    "00FFFF",  # Cyan
    "00FF9F",  # Spring Green
    "00E5FF",  # Bright Cyan
    "1E90FF",  # Dodger Blue
    "4169E1",  # Royal Blue
    "6495ED",  # Cornflower Blue
    "7B68EE",  # Medium Slate Blue
    "9370DB",  # Medium Purple
    "BA55D3",  # Medium Orchid
    "DA70D6",  # Orchid
    "FF69B4",  # Hot Pink
    "FF1493",  # Deep Pink
    "FF6347",  # Tomato
    "FF7F50",  # Coral
    "FFA500",  # Orange
    "FFD700",  # Gold
    "F0E68C",  # Khaki
    "ADFF2F",  # Green Yellow
    "7FFF00",  # Chartreuse
    "00FF00",  # Lime
    "32CD32",  # Lime Green
    "90EE90",  # Light Green
    "00FA9A",  # Medium Spring Green
    "40E0D0",  # Turquoise
    "48D1CC",  # Medium Turquoise
    "00CED1",  # Dark Turquoise
    "5F9EA0",  # Cadet Blue
    "B0C4DE",  # Light Steel Blue
    "ADD8E6",  # Light Blue
    "87CEEB",  # Sky Blue
    "87CEFA",  # Light Sky Blue
    "DDA0DD",  # Plum
    "EE82EE",  # Violet
    "D8BFD8",  # Thistle
    "FFB6C1",  # Light Pink
    "FFC0CB",  # Pink
    "F08080",  # Light Coral
    "FA8072",  # Salmon
    "E9967A",  # Dark Salmon
    "FFA07A",  # Light Salmon
    "FF8C00",  # Dark Orange
    "FFDAB9",  # Peach Puff
    "FFE4B5",  # Moccasin
    "FFEFD5",  # Papaya Whip
    "F5DEB3",  # Wheat
    "DEB887",  # Burlywood
]


def get_random_color():
    """Get a random crystal color for dark backgrounds"""
    return f"[{random.choice(CRYSTAL_COLORS)}]"


def create_separator(char="-", length=20):
    """Create a decorative separator line with max 20 characters"""
    return char * min(length, 20)


def format_message(title, content, footer="Follow on Instagram\n@1onlysarkar"):
    """
    Format a message with professional and friendly tone
    
    Args:
        title: Message title
        content: Message content (can be multi-line)
        footer: Message footer (default: Instagram info)
    
    Returns:
        Formatted message string with proper alignment and spacing
    """
    parts = []
    
    # Top spacing
    parts.append(f"{get_random_color()} ")
    
    # Title section - centered
    parts.append(f"{get_random_color()}  {title.upper()}")
    parts.append(f"{get_random_color()} ")
    parts.append(f"{get_random_color()}{create_separator('-')}")
    parts.append(f"{get_random_color()} ")
    
    # Content section with proper spacing
    for line in content.split('\n'):
        if line.strip():
            parts.append(f"{get_random_color()} {line.strip()}")
    
    # Bottom spacing
    parts.append(f"{get_random_color()} ")
    parts.append(f"{get_random_color()}{create_separator('-')}")
    parts.append(f"{get_random_color()} ")
    
    # Footer section
    for line in footer.split('\n'):
        if line.strip():
            parts.append(f"{get_random_color()}{line.strip()}")
    
    parts.append(f"{get_random_color()} ")
    
    return "[B][C]" + "\n".join(parts)


def format_greeting():
    """Format a warm greeting message"""
    title = "Welcome Friend"
    content = """Hey there

I am your Free Fire assistant
here to help you out

Type /help to see what I can do
for you"""
    return format_message(title, content)


def format_help():
    """Format the help command message with friendly tone - returns two parts"""
    # Part 1 - Squad Commands
    title1 = "Command Guide"
    content1 = """Here is what I can help you with
ㅤ
Squad Commands:
ㅤ
/5 - Accept squad invite
ㅤ
/x/[code] - Join squad
ㅤ
leave - Exit squad"""
    
    # Part 2 - Special Commands
    title2 = "Special Commands"
    content2 = """/spm/[times]/[uid] - Send invites
ㅤ
/s - Special function
ㅤ
@a [uid] [emote] - Emote attack
ㅤ
Feel free to use any command"""
    
    # Return both parts without footer
    part1 = format_message(title1, content1.strip(), footer="")
    part2 = format_message(title2, content2.strip(), footer="")
    
    return (part1, part2)


def format_squad_only():
    """Format squad-only command message with friendly tone"""
    title = "Oops"
    content = """This command works only in
squad chat
 
Please join a squad first and
try again"""
    return format_message(title, content)


def format_active_target(uid, uid_formatter):
    """Format active target message"""
    title = "Target Locked"
    content = f"""Target activated successfully
 
Player ID: {uid_formatter(uid)}
 
Ready to execute command"""
    return format_message(title, content)


def format_invitation_accepted():
    """Format invitation accepted message with friendly urgency"""
    title = "Squad Invitation"
    content = """Hey I have sent you an invite
 
Please accept it quickly so we
can team up together
 
Thanks"""
    return format_message(title, content)


def format_spam_confirmation(times, target_uid, uid_formatter):
    """Format spam confirmation message"""
    title = "Invites Sending"
    content = f"""Starting invitation process
 
Total Invites: {times}
Target Player: {uid_formatter(target_uid)}
 
Please wait while I send them"""
    return format_message(title, content)


def format_welcome_squad(owner_uid, uid_formatter):
    """Format welcome message when joining squad"""
    title = "Bot Active"
    content = f"""Hello everyone
 
I am now active and ready to
assist you
 
Squad Owner: {uid_formatter(owner_uid)}
 
Type /help to see all available
commands and features
 
Let us have a great game"""
    return format_message(title, content)
