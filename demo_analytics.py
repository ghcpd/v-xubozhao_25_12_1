"""
Demo script showcasing upgraded analytics capabilities
Demonstrates key libraries working together
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from scipy import stats
import io


def demo_analytics_pipeline():
    """Demonstrate a complete analytics workflow"""
    
    print("=" * 60)
    print("Backend Analytics Service - Demo")
    print("=" * 60)
    print()
    
    # 1. Data Generation
    print("📊 Step 1: Generating synthetic sales data...")
    np.random.seed(42)
    
    dates = pd.date_range('2024-01-01', periods=365, freq='D')
    sales = 1000 + np.cumsum(np.random.randn(365) * 50)  # Random walk
    revenue = sales * (100 + np.random.randn(365) * 10)
    
    df = pd.DataFrame({
        'date': dates,
        'sales': sales.astype(int),
        'revenue': revenue.astype(int)
    })
    
    print(f"✓ Generated {len(df)} days of data")
    print(f"  Sales range: ${df['sales'].min():,} - ${df['sales'].max():,}")
    print(f"  Revenue range: ${df['revenue'].min():,} - ${df['revenue'].max():,}")
    print()
    
    # 2. Statistical Analysis
    print("📈 Step 2: Performing statistical analysis...")
    
    # Calculate statistics
    sales_mean = df['sales'].mean()
    sales_std = df['sales'].std()
    revenue_mean = df['revenue'].mean()
    
    # Correlation test
    correlation, p_value = stats.pearsonr(df['sales'], df['revenue'])
    
    print(f"✓ Sales Statistics:")
    print(f"  Mean: ${sales_mean:,.2f}")
    print(f"  Std Dev: ${sales_std:,.2f}")
    print(f"✓ Revenue Mean: ${revenue_mean:,.2f}")
    print(f"✓ Sales-Revenue Correlation: {correlation:.3f} (p={p_value:.4f})")
    print()
    
    # 3. Machine Learning - Trend Prediction
    print("🤖 Step 3: Building predictive model...")
    
    # Prepare data for regression
    X = np.arange(len(df)).reshape(-1, 1)
    y = df['sales'].values
    
    # Train model
    model = LinearRegression()
    model.fit(X, y)
    predictions = model.predict(X)
    
    r2 = r2_score(y, predictions)
    slope = model.coef_[0]
    
    print(f"✓ Linear Regression Model:")
    print(f"  R² Score: {r2:.4f}")
    print(f"  Trend: {slope:+.2f} sales/day")
    print()
    
    # 4. Advanced Analytics with Pandas
    print("📊 Step 4: Time-based aggregation...")
    
    df['month'] = df['date'].dt.to_period('M')
    monthly = df.groupby('month').agg({
        'sales': ['sum', 'mean', 'std'],
        'revenue': ['sum', 'mean']
    }).round(2)
    
    print(f"✓ Monthly aggregation complete")
    print(f"  Total months: {len(monthly)}")
    print(f"  Best month (revenue): {monthly['revenue']['sum'].idxmax()}")
    print()
    
    # 5. Data Visualization
    print("📉 Step 5: Creating visualizations...")
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Plot 1: Sales over time
    axes[0, 0].plot(df['date'], df['sales'], linewidth=1, alpha=0.7)
    axes[0, 0].plot(df['date'], predictions, 'r--', linewidth=2, label='Trend')
    axes[0, 0].set_title('Daily Sales with Trend Line', fontsize=12, fontweight='bold')
    axes[0, 0].set_xlabel('Date')
    axes[0, 0].set_ylabel('Sales')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)
    
    # Plot 2: Revenue distribution
    axes[0, 1].hist(df['revenue'], bins=30, edgecolor='black', alpha=0.7)
    axes[0, 1].set_title('Revenue Distribution', fontsize=12, fontweight='bold')
    axes[0, 1].set_xlabel('Revenue ($)')
    axes[0, 1].set_ylabel('Frequency')
    axes[0, 1].grid(True, alpha=0.3)
    
    # Plot 3: Sales vs Revenue scatter
    axes[1, 0].scatter(df['sales'], df['revenue'], alpha=0.5, s=20)
    axes[1, 0].set_title(f'Sales vs Revenue (r={correlation:.3f})', fontsize=12, fontweight='bold')
    axes[1, 0].set_xlabel('Sales')
    axes[1, 0].set_ylabel('Revenue ($)')
    axes[1, 0].grid(True, alpha=0.3)
    
    # Plot 4: Monthly revenue trend
    monthly_revenue = df.groupby('month')['revenue'].sum()
    axes[1, 1].bar(range(len(monthly_revenue)), monthly_revenue.values, alpha=0.7)
    axes[1, 1].set_title('Monthly Revenue', fontsize=12, fontweight='bold')
    axes[1, 1].set_xlabel('Month')
    axes[1, 1].set_ylabel('Total Revenue ($)')
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Save to buffer (in real scenario would save to file)
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=100, bbox_inches='tight')
    buf.seek(0)
    
    print(f"✓ Created 4 visualization plots")
    print(f"  Chart size: {len(buf.read()) / 1024:.1f} KB")
    
    plt.close(fig)
    print()
    
    # 6. Summary Report
    print("=" * 60)
    print("📋 ANALYSIS SUMMARY")
    print("=" * 60)
    print(f"Dataset: {len(df)} days of sales data")
    print(f"Average daily sales: ${sales_mean:,.2f}")
    print(f"Average daily revenue: ${revenue_mean:,.2f}")
    print(f"Sales trend: {slope:+.2f} units/day")
    print(f"Correlation strength: {correlation:.3f} ({'Strong' if abs(correlation) > 0.7 else 'Moderate'})")
    print(f"Model performance (R²): {r2:.4f}")
    print("=" * 60)
    print()
    print("✅ All upgraded libraries working correctly!")
    print()
    
    return df, model


if __name__ == '__main__':
    demo_analytics_pipeline()
