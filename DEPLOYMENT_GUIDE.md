# CineMind AI - Free Deployment Guide

## 🚀 DEPLOYMENT STEPS

### 📁 STEP 1: CREATE GITHUB REPOSITORY

1. Go to https://github.com/new
2. Repository name: `cinemind-ai`
3. Description: `AI Powered Movie Recommendations`
4. Make it **Public** (required for free hosting)
5. **DO NOT** initialize with README (we already have code)
6. Click "Create repository"

### 📁 STEP 2: PUSH TO GITHUB

```bash
# Replace YOUR_USERNAME with your GitHub username
git remote add origin https://github.com/YOUR_USERNAME/cinemind-ai.git
git branch -M main
git push -u origin main
```

### 📁 STEP 3: DEPLOY BACKEND (RENDER)

1. Go to https://render.com
2. Sign up with **GitHub** (free)
3. Click "New Web Service"
4. Connect your GitHub account
5. Select the `cinemind-ai` repository
6. **Configure Service:**
   - **Name**: cinemind-backend
   - **Runtime**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main_peak:app --host 0.0.0.0 --port $PORT`
   - **Root Directory**: `backend`
7. Click "Create Web Service"

**Wait 2-5 minutes for deployment**

**Your backend URL will be:** `https://cinemind-backend.onrender.com`

### 📁 STEP 4: DEPLOY FRONTEND (VERCEL)

1. Go to https://vercel.com
2. Sign up with **GitHub** (free)
3. Click "New Project"
4. Import the `cinemind-ai` repository
5. **Configure Project:**
   - **Framework Preset**: Next.js
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `.next`
6. **Environment Variables:**
   - **NEXT_PUBLIC_API_BASE**: `https://cinemind-backend.onrender.com/api/v1`
7. Click "Deploy"

**Wait 1-3 minutes for deployment**

**Your frontend URL will be:** `https://cinemind-ai.vercel.app`

### 📁 STEP 5: TEST DEPLOYMENT

1. Visit your frontend URL
2. Test movie search
3. Test user registration
4. Test recommendations

## 🔧 TROUBLESHOOTING

### ❌ Backend Not Loading
- Wait 5-10 minutes (Render cold start)
- Check Render logs for errors
- Ensure `requirements.txt` exists

### ❌ Frontend API Errors
- Verify `NEXT_PUBLIC_API_BASE` is correct
- Check CORS settings (already configured)
- Ensure backend is deployed first

### ❌ Database Issues
- SQLite will reset on redeploy (acceptable for demo)
- Movie dataset loads from cache automatically

## 🎯 FINAL RESULT

**Your Public URL:** `https://cinemind-ai.vercel.app`

**Features Available:**
- ✅ Movie search (30,981+ movies)
- ✅ User authentication
- ✅ Genre recommendations
- ✅ Similar movie recommendations
- ✅ Watchlist functionality
- ✅ Premium UI design

## 💰 COST BREAKDOWN

**Frontend (Vercel):** $0/month
- Unlimited bandwidth
- 100GB storage
- Custom domain support

**Backend (Render):** $0/month
- 750 hours/month (enough for demo)
- Free SSL certificate
- Automatic deployments

**Total Cost:** $0/month

## 🚀 UPGRADE PATH

If you need better performance later:
- **Render Pro**: $7/month (no cold starts)
- **Vercel Pro**: $20/month (more bandwidth)
- **Database**: PostgreSQL ($7/month)

---

**🎉 Your CineMind AI will be live and shareable!**

**Deploy now and share your AI movie recommendation app!**
