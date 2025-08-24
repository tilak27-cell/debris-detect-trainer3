# Deploying to Vercel

## Prerequisites
1. Node.js and npm installed
2. Vercel CLI installed: `npm install -g vercel`
3. Vercel account (free tier is sufficient)

## Deployment Steps

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy**
   ```bash
   vercel --prod
   ```
   - Follow the prompts to link to your Vercel account
   - Choose the default options for all prompts

4. **After Deployment**
   - Your app will be available at `https://your-app-name.vercel.app`
   - You can find the URL in the Vercel dashboard

## Environment Variables
If your app needs any environment variables (like API keys), set them in the Vercel dashboard:
1. Go to your project in Vercel
2. Navigate to Settings > Environment Variables
3. Add your variables
4. Redeploy your application

## Important Notes
- Vercel has a 10-second execution limit for serverless functions
- For file uploads, consider using Vercel Blob or an external storage service
- Check the Vercel dashboard for logs and monitoring
