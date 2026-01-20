# Клиника Игоря Дара - Website

This project is a static website for "Клиника Игоря Дара". It contains HTML, CSS, JS assets and forms integrated with Web3Forms.

## Structure
- `index.html`: Main landing page.
- `thank-you.html`: Success page for form submissions.
- `assets/`: Images and other static assets.
- `scripts/`: Maintenance scripts (e.g., `update_forms.py`).
- Subdirectories (e.g., `lechenie-depressii/`): Landing pages for specific services.

## Deployment

### Vercel
1.  Push this repository to GitHub.
2.  Log in to [Vercel](https://vercel.com/).
3.  Click "Add New..." -> "Project".
4.  Import the GitHub repository.
5.  Vercel will automatically detect the static site structure.
6.  Click "Deploy".

### Form Configuration
Forms are configured to use [Web3Forms](https://web3forms.com/).
- Access Key: `78c1b7d4-b1b3-4c53-831c-0f1649313701`
- Recipient: `profitcleaning@gmail.com`

To update forms, modify `scripts/update_forms.py` and run it to batch update all sub-pages.
