# Harvey Rendall Personal Website

A modern, responsive personal website built with HTML, Tailwind CSS, and vanilla JavaScript. Features a clean design with dark/light mode, side navigation, and easy content management.

## 🚀 Features

- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Dark/Light Mode**: Toggle between themes with persistent preference
- **Side Navigation**: Clean, accessible navigation bar
- **Modern Typography**: Sophisticated font pairing for professional appearance
- **Easy Content Management**: Simple HTML structure for easy updates
- **Fast Loading**: Optimized for performance
- **Accessible**: Built with accessibility best practices

## 📁 Project Structure

```
harveyrendall.com/
├── index.html              # Home page
├── about.html              # About me page
├── travels.html            # Travel blog
├── articles.html           # Articles and writing (temporarily hidden)
├── projects.html           # Portfolio and projects
├── cv.html                 # CV and resume
├── contact.html            # Contact information
├── tutoring.html           # Tutoring services
├── assets/
│   ├── css/
│   │   └── style.css      # Custom styles
│   ├── js/
│   │   └── script.js      # JavaScript functionality
│   └── images/            # Image assets
└── README.md              # This file
```

### 📝 Note: Articles Section Temporarily Hidden
The articles section has been temporarily hidden from the navigation but the files remain in the codebase for future use. To restore the articles section:
1. Uncomment the articles navigation links in all HTML files
2. Uncomment the articles quick link card in `index.html`
3. Update the JavaScript dropdown arrays to include 'articles'
4. Update meta descriptions and welcome text to include articles

## 🎨 Design Features

- **Side Navigation**: Fixed sidebar with smooth hover effects
- **Theme Toggle**: Sun/moon icon for dark/light mode switching
- **Card-based Layout**: Clean, organized content presentation
- **Gradient Accents**: Subtle gradients for visual interest
- **Smooth Animations**: Hover effects and transitions
- **Professional Typography**: Carefully chosen font combinations

## 🎯 Typography & Font Customization

### Current Font Setup
The website uses a sophisticated font combination:

**Primary Font (Body Text)**: Inter
- Modern, highly readable sans-serif
- Perfect for screens and digital content
- Clean and professional

**Display Font (Headings)**: Playfair Display
- Elegant serif font for headings
- Adds sophistication and maturity
- Beautiful contrast with body text

### How to Change Fonts

#### Option 1: Quick Font Swaps
Replace the Google Fonts link in the `<head>` section of each HTML file:

**For Inter + Playfair Display (Current)**:
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap" rel="stylesheet">
```

**For Source Sans Pro + Merriweather**:
```html
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@300;400;600;700&family=Merriweather:wght@300;400;700&display=swap" rel="stylesheet">
```

**For Open Sans + Lora**:
```html
<link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;700&family=Lora:wght@400;500;600;700&display=swap" rel="stylesheet">
```

#### Option 2: Update Font Configuration
After changing the Google Fonts link, update the Tailwind configuration in each HTML file:

```javascript
tailwind.config = {
    darkMode: 'class',
    theme: {
        extend: {
            fontFamily: {
                'sans': ['Your New Sans Font', 'ui-sans-serif', 'system-ui', 'sans-serif'],
                'display': ['Your New Serif Font', 'serif'],
            }
        }
    }
}
```

#### Option 3: CSS Customization
Update the font families in `assets/css/style.css`:

```css
body {
    font-family: 'Your New Sans Font', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Your New Serif Font', serif;
}
```

### Recommended Font Combinations

1. **Inter + Playfair Display** (Current) - Modern & Elegant
2. **Source Sans Pro + Merriweather** - Professional & Sophisticated
3. **Open Sans + Lora** - Clean & Beautiful
4. **Inter + Source Serif Pro** - Modern & Readable
5. **Roboto + Roboto Slab** - Google's Professional Choice

## 📝 Content Management

### Adding New Pages
1. Create a new HTML file (e.g., `newpage.html`)
2. Copy the structure from an existing page
3. Update the navigation links in all pages
4. Add your content in the marked sections

### Adding Content Cards
Each page has clearly marked sections for content. Look for comments like:
```html
<!-- CONTENT CARD START -->
<div class="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6">
    <!-- Your content here -->
</div>
<!-- CONTENT CARD END -->
```

### Navigation Updates
To add a new page to navigation, update the navigation section in all HTML files:
```html
<!-- New Page Link -->
<li>
    <a href="newpage.html" class="flex items-center px-4 py-3 text-gray-700 dark:text-gray-300 hover:bg-blue-50 dark:hover:bg-gray-700 hover:text-blue-600 dark:hover:text-blue-400 rounded-lg transition-colors duration-200">
        <svg class="w-5 h-5 mr-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <!-- Icon path -->
        </svg>
        New Page
    </a>
</li>
```

## 🚀 Deployment

### Option 1: Netlify (Recommended)
1. Push your code to GitHub
2. Connect your repository to Netlify
3. Deploy automatically on every push

### Option 2: Vercel
1. Push your code to GitHub
2. Connect your repository to Vercel
3. Deploy automatically on every push

### Option 3: GitHub Pages
1. Push your code to GitHub
2. Enable GitHub Pages in repository settings
3. Select source branch (usually `main`)

### Option 4: Manual Upload
1. Upload all files to your web hosting provider
2. Ensure all file paths are correct
3. Test all functionality

## 💻 Local Development

### Method 1: Simple File Opening
```bash
open index.html
```
- Opens in your default browser
- Works immediately

### Method 2: Python HTTP Server (Recommended)
```bash
python3 -m http.server 8000
```
- Visit: http://localhost:8000
- Better for development
- All features work properly

### Method 3: Node.js HTTP Server
```bash
npx serve .
```
- Visit: http://localhost:3000
- Modern development server

## 🌐 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## 🎨 Color Scheme

### Light Mode
- Background: `#f9fafb` (gray-50)
- Text: `#111827` (gray-900)
- Cards: `#ffffff` (white)
- Accent: `#2563eb` (blue-600)

### Dark Mode
- Background: `#111827` (gray-900)
- Text: `#f9fafb` (gray-50)
- Cards: `#1f2937` (gray-800)
- Accent: `#3b82f6` (blue-500)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Feel free to fork this project and customize it for your own needs. If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

---

Built with ❤️ using HTML, Tailwind CSS, and vanilla JavaScript.
