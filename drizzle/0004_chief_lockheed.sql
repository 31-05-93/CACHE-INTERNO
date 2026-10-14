CREATE TABLE `cxc_projections` (
	`id` text PRIMARY KEY NOT NULL,
	`period` text NOT NULL,
	`pdf_report_id` text NOT NULL,
	`sales_report_id` text NOT NULL,
	`selections` text DEFAULT '[]' NOT NULL,
	`mappings` text DEFAULT '{}' NOT NULL,
	`version` integer DEFAULT 1 NOT NULL,
	`updated_at` text NOT NULL,
	`updated_by` text NOT NULL
);
--> statement-breakpoint
CREATE TABLE `cxc_sales_reports` (
	`id` text PRIMARY KEY NOT NULL,
	`year` integer NOT NULL,
	`name` text NOT NULL,
	`currency` text NOT NULL,
	`file_key` text NOT NULL,
	`created_at` text NOT NULL,
	`created_by` text NOT NULL,
	`status` text DEFAULT 'importing' NOT NULL
);
--> statement-breakpoint
CREATE TABLE `cxc_sales_rows` (
	`id` text PRIMARY KEY NOT NULL,
	`report_id` text NOT NULL,
	`period` text NOT NULL,
	`record` text NOT NULL
);
