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

            views.setOnClickPendingIntent(R.id.btn_snap_item, getDeepLinkIntent(context, "camera", 1))
            views.setOnClickPendingIntent(R.id.jump_closet, getDeepLinkIntent(context, "closet", 2))
            views.setOnClickPendingIntent(R.id.jump_scent, getDeepLinkIntent(context, "scent", 3))
            views.setOnClickPendingIntent(R.id.jump_sales, getDeepLinkIntent(context, "sales", 4))
            views.setOnClickPendingIntent(R.id.jump_pinterest, getDeepLinkIntent(context, "pinterest", 5))
            views.setOnClickPendingIntent(R.id.jump_fyp_preview, getDeepLinkIntent(context, "pinterest", 6))

            appWidgetManager.updateAppWidget(appWidgetId, views)
        }
    }

    private fun getDeepLinkIntent(context: Context, route: String, req: Int): PendingIntent {
        val intent = Intent(context, MainActivity::class.java).apply {
            action = Intent.ACTION_VIEW
            data = Uri.parse("https://localhost/#$route")
            flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TOP or Intent.FLAG_ACTIVITY_SINGLE_TOP
        }
        return PendingIntent.getActivity(context, req, intent, PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE)
    }
}
