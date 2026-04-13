CREATE TABLE IF NOT EXISTS "comments_comment" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "username" varchar(50) NOT NULL,
    "email" varchar(254) NOT NULL,
    "homepage" varchar(200) NULL,
    "text" text NOT NULL,
    "created_at" datetime NOT NULL,
    "parent_id" bigint NULL REFERENCES "comments_comment" ("id") DEFERRABLE INITIALLY DEFERRED,
    "file" varchar(100) NULL
);

CREATE INDEX "comments_comment_parent_id_3e0802fb"
ON "comments_comment" ("parent_id");
