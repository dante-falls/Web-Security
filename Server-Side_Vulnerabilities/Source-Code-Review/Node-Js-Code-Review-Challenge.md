<h1>Node.js Code Review Challenge</h1>

Identify the potential vulnerabilities in the following Node.js code snippet

```
const express = require("express");
const crypto = require("crypto");
const db = require("./db");

const app = express();

app.use(express.json());

function authenticate(req, res, next) {
    const token = req.headers["authorization"];

    if (!token) {
        return res.status(401).json({ error: "Authentication required" });
    }

    const session = db.sessions.findOne({ token });

    if (!session) {
        return res.status(401).json({ error: "Invalid session" });
    }

    req.user = db.users.findOne({ id: session.userId });
    next();
}

app.get("/api/projects/:projectId", authenticate, async (req, res) => {
    const project = await db.projects.findOne({
        id: req.params.projectId
    });

    if (!project) {
        return res.status(404).json({ error: "Project not found" });
    }

    res.json({
        id: project.id,
        name: project.name,
        ownerId: project.ownerId,
        members: project.members
    });
});

app.post("/api/projects/:projectId/members", authenticate, async (req, res) => {
    const project = await db.projects.findOne({
        id: req.params.projectId
    });

    if (!project) {
        return res.status(404).json({ error: "Project not found" });
    }

    if (project.ownerId !== req.user.id) {
        return res.status(403).json({ error: "Only the owner can modify members" });
    }

    const { userId, role } = req.body;

    project.members.push({
        userId,
        role
    });

    await db.projects.updateOne(
        { id: project.id },
        { $set: { members: project.members } }
    );

    res.json({ success: true });
});

app.post("/api/projects/:projectId/export", authenticate, async (req, res) => {
    const project = await db.projects.findOne({
        id: req.params.projectId
    });

    if (!project) {
        return res.status(404).json({ error: "Project not found" });
    }

    const exportToken = crypto.randomBytes(16).toString("hex");

    await db.exports.insertOne({
        token: exportToken,
        projectId: project.id,
        requestedBy: req.user.id
    });

    res.json({
        downloadUrl: `/exports/${exportToken}`
    });
});

app.get("/exports/:token", async (req, res) => {
    const exportJob = await db.exports.findOne({
        token: req.params.token
    });

    if (!exportJob) {
        return res.status(404).send("Not found");
    }

    const project = await db.projects.findOne({
        id: exportJob.projectId
    });

    res.setHeader("Content-Type", "application/json");

    res.send(JSON.stringify({
        project: project,
        exportedFor: exportJob.requestedBy
    }));
});

app.post("/api/search", authenticate, async (req, res) => {
    const { query } = req.body;

    const results = await db.projects.find({
        $where: `function() {
            return this.name.toLowerCase().includes("${query.toLowerCase()}");
        }`
    });

    res.json(results);
});

app.post("/api/profile", authenticate, async (req, res) => {
    const profile = await db.users.findOne({
        id: req.user.id
    });

    Object.assign(profile, req.body);

    await db.users.updateOne(
        { id: profile.id },
        { $set: profile }
    );

    res.json(profile);
});

app.listen(3000);
```
