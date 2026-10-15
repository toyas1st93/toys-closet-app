package com.toyscloset.app

import android.app.PendingIntent
import android.appwidget.AppWidgetManager
import android.appwidget.AppWidgetProvider
import android.content.Context
import android.content.Intent
import android.net.Uri
import android.widget.RemoteViews

class ClosetWidgetProvider : AppWidgetProvider() {
    override fun onUpdate(context: Context, appWidgetManager: AppWidgetManager, appWidgetIds: IntArray) {
        for (appWidgetId in appWidgetIds) {
            val views = RemoteViews(context.packageName, R.layout.widget_layout)

            views.setOnClickPendingIntent(R.id.btn_snap_item, getPendingUrl(context, "https://toys-wardrobe.netlify.app#camera", 1))
            views.setOnClickPendingIntent(R.id.jump_closet, getPendingUrl(context, "https://toys-wardrobe.netlify.app#closet", 2))
            views.setOnClickPendingIntent(R.id.jump_scent, getPendingUrl(context, "https://toys-wardrobe.netlify.app#scent", 3))
            views.setOnClickPendingIntent(R.id.jump_events, getPendingUrl(context, "https://toys-wardrobe.netlify.app#events", 4))
            views.setOnClickPendingIntent(R.id.jump_planner, getPendingUrl(context, "https://toys-wardrobe.netlify.app#planner", 5))

            appWidgetManager.updateAppWidget(appWidgetId, views)
        }
    }

    private fun getPendingUrl(context: Context, url: String, req: Int): PendingIntent {
        val intent = Intent(Intent.ACTION_VIEW, Uri.parse(url)).apply {
            flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TOP
        }
        return PendingIntent.getActivity(context, req, intent, PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE)
    }
}
